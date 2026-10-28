"""
========================================================================================
Projeto: NovaMétrica Analytics & Entregáveis Inteligentes (Antigravity CLI + Gemini)
Script: 07_scripts_exploratorios/02_atualizar_matriz_priorizacao.py
Descrição: Atualiza a planilha de Matriz Esforço x Impacto com as 4 iniciativas 
           estratégicas deliberadas pelo diagnóstico analítico.
Módulo: 07_scripts_exploratorios (Evidências Algorítmicas e Rastreabilidade)
Autor: Estrategista de Negócios & Engenheiro de Dados Sênior
========================================================================================
"""

from pathlib import Path
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Assegura suporte a UTF-8 no terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

def _obter_raiz_projeto() -> Path:
    dir_atual = Path(__file__).resolve().parent
    if dir_atual.name == "07_scripts_exploratorios":
        return dir_atual.parent
    return Path(".")

BASE_DIR = _obter_raiz_projeto()
EXCEL_PATH = BASE_DIR / "06_entregaveis_estrategicos" / "matriz_esforco_impacto_priorizacao.xlsx"

def criar_ou_atualizar_matriz():
    print(f"[*] Carregando e estruturando a Matriz de Priorização em: 06_entregaveis_estrategicos/{EXCEL_PATH.name}")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matriz_Priorizacao"

    # Estilos Visuais Corporativos (NovaMétrica Dark Navy Theme)
    header_fill = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    data_font = Font(name="Segoe UI", size=10)
    bold_font = Font(name="Segoe UI", size=10, bold=True)
    
    # Cores de Classificação (Badges)
    fill_p1 = PatternFill(start_color="FFEBEE", end_color="FFEBEE", fill_type="solid") # Vermelho suave
    font_p1 = Font(name="Segoe UI", size=10, bold=True, color="C62828")
    
    fill_p2 = PatternFill(start_color="FFF3E0", end_color="FFF3E0", fill_type="solid") # Laranja suave
    font_p2 = Font(name="Segoe UI", size=10, bold=True, color="EF6C00")
    
    fill_p3 = PatternFill(start_color="E8F5E9", end_color="E8F5E9", fill_type="solid") # Verde suave
    font_p3 = Font(name="Segoe UI", size=10, bold=True, color="2E7D32")
    
    fill_p4 = PatternFill(start_color="E3F2FD", end_color="E3F2FD", fill_type="solid") # Azul suave
    font_p4 = Font(name="Segoe UI", size=10, bold=True, color="1565C0")

    thin_border = Border(
        left=Side(style="thin", color="CCCCCC"),
        right=Side(style="thin", color="CCCCCC"),
        top=Side(style="thin", color="CCCCCC"),
        bottom=Side(style="thin", color="CCCCCC"),
    )

    headers = [
        "ID",
        "Iniciativa / Ação Estratégica",
        "Classificação na Matriz",
        "Impacto",
        "Esforço",
        "Prioridade",
        "Evidência Interna [CONFIRMADO]",
        "Impacto Estimado (R$ / Operacional)",
        "Responsável Sugerido",
        "Prazo de Execução",
        "Status de Aprovação",
    ]

    ws.append(headers)

    # 4 Iniciativas Estratégicas Deliberadas
    dados = [
        [
            "ACT-01",
            "Emissão emergencial de Pedido de Compra (PO) de reposição de 30 unidades para EL-001, CA-003 e MO-002",
            "Quick Win (Alto Impacto, Baixo Esforço)",
            "Alto",
            "Baixo",
            "P1 (Crítica)",
            "Saldo atual de apenas 5 un por SKU vs. estoque mínimo de 12 un. Cobertura crítica de 10,6 dias e faturamento de R$ 669,69/dia em risco.",
            "Evita perda de receita projetada de R$ 20.090,72/mês por ruptura e restabelece margem de segurança de 60 dias.",
            "Gerência de Suprimentos & Operações",
            "Imediato (7 dias)",
            "Aprovado C-Level",
        ],
        [
            "ACT-02",
            "Redesenho da política da Semana do Consumidor (trava de desconto em 12% ou condicionamento de 18% a combos/bundles de alta margem)",
            "Projeto Estratégico (Alto Impacto, Médio Esforço)",
            "Alto",
            "Médio",
            "P2 (Alta)",
            "Semana do Consumidor destruiu 8,98 p.p. de margem (34,99% vs. 43,97% regular) com desconto médio de 17,95% sem gerar escala de volume (apenas 29 pedidos).",
            "Recuperação de 5 a 7 p.p. de margem bruta nas próximas campanhas promocionais, blindando rentabilidade.",
            "Diretoria Comercial & Marketing",
            "Curto Prazo (30 dias)",
            "Aprovado C-Level",
        ],
        [
            "ACT-03",
            "Implementação obrigatória do campo 'Motivo_Devolucao' no fluxo reverso de devolução do SAC/E-commerce para auditoria de produto",
            "Melhoria Contínua (Médio Impacto, Baixo Esforço)",
            "Médio",
            "Baixo",
            "P3 (Média)",
            "Pedidos devolvidos chegam 0,48 dias mais rápido que os normais (4,85d vs. 5,33d; r=+0,0732), isentando frete e apontando falha intrínseca de produto/expectativa.",
            "Elimina lacuna crítica de dados [DADO AUSENTE] e permite correções de ficha técnica, embalagem ou recall pontual.",
            "Gerência de Atendimento & SAC",
            "Curto Prazo (30 dias)",
            "Aprovado C-Level",
        ],
        [
            "ACT-04",
            "Campanha promocional direcionada de queima de estoque parado para itens com cobertura excessiva (ES-001/ES-003, PT-002 e SP-002)",
            "Otimização de Capital (Médio Impacto, Baixo Esforço)",
            "Médio",
            "Baixo",
            "P4 (Média)",
            "Itens com 40 unidades estocadas, até 28 dias sem venda e cobertura de capital superior a 90 dias sem giro adequado.",
            "Desmobilização de capital de giro de ~R$ 35.000,00 estagnado, liberando espaço físico no armazém e fluxo de caixa.",
            "Gerência Comercial & Pricing",
            "Médio Prazo (90 dias)",
            "Aprovado C-Level",
        ],
    ]

    for row in dados:
        ws.append(row)

    # Formatação Visual da Planilha
    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[1].height = 28

    # Formatação das linhas de dados
    for row_idx, row_cells in enumerate(ws.iter_rows(min_row=2, max_row=len(dados) + 1, min_col=1, max_col=len(headers)), start=2):
        ws.row_dimensions[row_idx].height = 45
        prioridade_val = ws.cell(row=row_idx, column=6).value
        
        for col_idx, cell in enumerate(row_cells, start=1):
            cell.font = data_font
            cell.border = thin_border
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            
            # Centralizar colunas curtas
            if col_idx in [1, 3, 4, 5, 6, 9, 10, 11]:
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            
            # Badges de destaque por prioridade
            if col_idx == 6:
                if "P1" in str(prioridade_val):
                    cell.fill = fill_p1
                    cell.font = font_p1
                elif "P2" in str(prioridade_val):
                    cell.fill = fill_p2
                    cell.font = font_p2
                elif "P3" in str(prioridade_val):
                    cell.fill = fill_p3
                    cell.font = font_p3
                elif "P4" in str(prioridade_val):
                    cell.fill = fill_p4
                    cell.font = font_p4

    # Larguras ideais das colunas
    larguras = {
        "A": 10,  # ID
        "B": 36,  # Iniciativa
        "C": 26,  # Classificação
        "D": 12,  # Impacto
        "E": 12,  # Esforço
        "F": 16,  # Prioridade
        "G": 38,  # Evidência
        "H": 34,  # Impacto Estimado
        "I": 24,  # Responsável
        "J": 18,  # Prazo
        "K": 20,  # Status
    }
    for col_letter, width in larguras.items():
        ws.column_dimensions[col_letter].width = width

    EXCEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    wb.save(EXCEL_PATH)
    print(f"[OK] Planilha '{EXCEL_PATH.name}' atualizada com sucesso com as 4 iniciativas prioritárias!")

if __name__ == "__main__":
    criar_ou_atualizar_matriz()
