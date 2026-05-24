from pathlib import Path
from datetime import datetime
import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet
#import matplotlib.pyplot as plt
#total_vendido_no_periodo, produto_mais_vendido_por_receita, categoria_que_vendeu_mais, regiao_que_mais_vendeu, sales_rep_que_mais_vendeu

def generate_report(df, metrics):
    # Define o caminho absoluto para a pasta de saída (raiz do projeto/output)
    base_path = Path(__file__).parent.parent
    output_dir = base_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    path = str(output_dir / "relatorio.xlsx")

    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, sheet_name="dados_brutos", index=False)

        metrics["produto_top"].to_excel(writer, sheet_name="produtos_mais_vendidos")
        metrics["categoria_top"].to_excel(writer, sheet_name="categorias_mais_vendidas")
        metrics["regiao_top"].to_excel(writer, sheet_name="regioes_com_mais_vendas")
        metrics["vendedor_top"].to_excel(writer, sheet_name="vendedores_com_mais_vendas")

        

    return path

def _format_currency(value):
    """
    Auxiliar para formatar valores no padrão monetário brasileiro (Ex: R$ 1.234,56).
    """
    try:
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return "R$ 0,00"

def generate_pdf(df_clean, metrics):
    """
    Gera um relatório PDF executivo, profissional e minimalista.
    Organizado com tabelas para facilitar a leitura e compatível com PyInstaller.
    """
    base_path = Path(__file__).parent.parent
    output_dir = base_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = str(output_dir / "relatorio.pdf")

    try:
        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )
        
        styles = getSampleStyleSheet()
        # Personalização leve para o estilo corporativo
        styles["Title"].fontSize = 18
        styles["Title"].spaceAfter = 12
        
        elements = []
        
        # --- 1. Título e Metadados ---
        elements.append(Paragraph("Relatório de Performance de Vendas", styles["Title"]))
        
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        elements.append(Paragraph(f"Data de Emissão: {timestamp}", styles["Normal"]))
        elements.append(Spacer(1, 30))

        # --- 2. Resumo Executivo ---
        elements.append(Paragraph("1. Resumo Executivo", styles["Heading2"]))
        elements.append(Spacer(1, 12))
        
        summary_data = [
            ["Métrica Principal", "Valor / Nome"],
            ["Faturamento Total", _format_currency(metrics.get("total_vendido", 0))],
            ["Produto Campeão", str(metrics["produto_top"].index[0])],
            ["Categoria Líder", str(metrics["categoria_top"].index[0])],
            ["Região com Maior Venda", str(metrics["regiao_top"].index[0])],
            ["Melhor Vendedor", str(metrics["vendedor_top"].index[0])]
        ]
        
        summary_table = Table(summary_data, colWidths=[200, 290])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.whitesmoke])
        ]))
        elements.append(summary_table)
        elements.append(Spacer(1, 40))

        # --- 3. Top 5 Produtos ---
        elements.append(Paragraph("2. Top 5 Produtos (por Receita)", styles["Heading3"]))
        elements.append(Spacer(1, 10))
        
        prod_data = [["Produto", "Receita Total"]]
        for prod, val in metrics["produto_top"].head(5).items():
            prod_data.append([prod, _format_currency(val)])
            
        prod_table = Table(prod_data, colWidths=[340, 150])
        prod_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('GRID', (0, 0), (-1, -1), 0.1, colors.grey),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]))
        elements.append(prod_table)
        elements.append(Spacer(1, 30))

        # --- 4. Top 5 Vendedores ---
        elements.append(Paragraph("3. Top 5 Vendedores (Desempenho Financeiro)", styles["Heading3"]))
        elements.append(Spacer(1, 10))
        
        vend_data = [["Vendedor", "Total Vendido"]]
        for vend, val in metrics["vendedor_top"].head(5).items():
            vend_data.append([vend, _format_currency(val)])
            
        vend_table = Table(vend_data, colWidths=[340, 150])
        vend_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('GRID', (0, 0), (-1, -1), 0.1, colors.grey),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]))
        elements.append(vend_table)

        # --- 5. Rodapé ---
        elements.append(Spacer(1, 80))
        footer = Paragraph(
            "<font size='8' color='grey'>Relatório gerado automaticamente. Uso interno e confidencial.</font>",
            styles["Italic"]
        )
        elements.append(footer)

        doc.build(elements)
        return pdf_path

    except Exception as e:
        raise RuntimeError(f"Erro crítico na geração do PDF: {e}")