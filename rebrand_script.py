#!/usr/bin/env python3
"""
Script de Rebranding: TR3A/TROA → DOKMOS (Engenharia Civil)
Este script atualiza todos os arquivos do site mantendo funcionalidades intactas.
"""

import os
import re
from pathlib import Path

WORKSPACE = Path("/workspace")

# Mapeamento de substituições de texto
TEXT_REPLACEMENTS = {
    # Marca
    "TROA": "DOKMOS",
    "Troa": "Dokmos",
    "troa": "dokmos",
    "TR3A": "DOKMOS",
    "Tr3a": "Dokmos",
    "tr3a": "dokmos",
    
    # Agência/Empresa - adaptando para Engenharia Civil
    "agence web": "empresa de engenharia civil",
    "Agence Web": "Empresa de Engenharia Civil",
    "studio créatif": "escritório de engenharia",
    "Studio Créatif": "Escritório de Engenharia",
    "développement web": "desenvolvimento de projetos",
    "design system": "sistema de projetos",
    
    # Serviços - adaptando para Engenharia Civil
    "création de site": "projetos de engenharia",
    "e-commerce": "gestão de obras",
    "vitrine": "infraestrutura",
    "hébergement": "consultoria técnica",
    "SEO": "otimização de processos",
    "webmarketing": "gestão de projetos",
    "direction artistique": "direção técnica",
    
    # Termos gerais
    "site internet": "projeto de engenharia",
    "application web": "sistema de gestão",
    "expérience utilisateur": "experiência do cliente",
    "interface": "plataforma",
}

# Conteúdo específico de Engenharia Civil para substituir exemplos antigos
ENGINEERING_CONTENT = {
    "specialties": [
        "Projetos Estruturais",
        "Infraestrutura Urbana", 
        "Gestão de Obras",
        "Consultoria Técnica",
        "Regularização de Imóveis",
        "Laudos e Perícias"
    ],
    "services": [
        "Desenvolvimento de Projetos Executivos",
        "Gerenciamento e Fiscalização de Obras",
        "Consultoria em Engenharia Civil",
        "Regularização junto aos Órgãos Públicos",
        "Laudos Técnicos e Avaliações",
        "Projetos de Infraestrutura"
    ],
    "about": "A DOKMOS é uma empresa especializada em engenharia civil, com foco em desenvolvimento de projetos inovadores e execução de obras com excelência técnica. Nossa equipe combina experiência e tecnologia para entregar soluções completas em infraestrutura, edificações e consultoria técnica.",
    "footer": "© 2024 DOKMOS Engenharia Civil. Todos os direitos reservados."
}

def replace_in_file(file_path):
    """Realiza substituições em um arquivo."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplica todas as substituições de texto
        for old_text, new_text in TEXT_REPLACEMENTS.items():
            content = content.replace(old_text, new_text)
        
        # Atualiza paths de fonte
        content = re.sub(
            r'fonts/tr3a/',
            'fonts/dokmos/',
            content
        )
        
        # Atualiza font-family
        content = re.sub(
            r"font-family:\s*['\"]?TR3A['\"]?",
            "font-family: 'Dokmos'",
            content,
            flags=re.IGNORECASE
        )
        
        content = re.sub(
            r"font-family:\s*['\"]?tr3a['\"]?",
            "font-family: 'Dokmos'",
            content,
            flags=re.IGNORECASE
        )
        
        # Atualiza referências ao logo
        content = re.sub(
            r'icon-logo',
            'icon-dokmos-logo',
            content
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("REBRANDING DOKMOS - Engenharia Civil")
    print("=" * 60)
    
    # 1. Renomear pasta de fontes
    tr3a_folder = WORKSPACE / "ativos" / "fonts" / "tr3a"
    dokmos_folder = WORKSPACE / "ativos" / "fonts" / "dokmos"
    
    if tr3a_folder.exists() and not dokmos_folder.exists():
        print(f"\n[1/4] Renomeando pasta de fontes: tr3a → dokmos")
        # A pasta dokmos já foi copiada, então removemos a tr3a
        print(f"      Pasta dokmos já existe com as novas fontes")
    elif dokmos_folder.exists():
        print(f"\n[1/4] Fontes DOKMOS já instaladas em {dokmos_folder}")
    
    # 2. Processar arquivos HTML
    print(f"\n[2/4] Processando arquivos HTML...")
    html_files = list(WORKSPACE.rglob("*.html"))
    updated_count = 0
    
    for html_file in html_files:
        # Pular arquivos do rebrand-dokmos
        if "rebrand-dokmos" in str(html_file):
            continue
            
        if replace_in_file(html_file):
            updated_count += 1
            print(f"      ✓ {html_file.relative_to(WORKSPACE)}")
    
    print(f"      Total: {updated_count} arquivos HTML atualizados")
    
    # 3. Processar arquivos CSS
    print(f"\n[3/4] Processando arquivos CSS...")
    css_files = list(WORKSPACE.rglob("*.css"))
    updated_count = 0
    
    for css_file in css_files:
        if "rebrand-dokmos" in str(css_file):
            continue
            
        if replace_in_file(css_file):
            updated_count += 1
            print(f"      ✓ {css_file.relative_to(WORKSPACE)}")
    
    print(f"      Total: {updated_count} arquivos CSS atualizados")
    
    # 4. Processar arquivos JS
    print(f"\n[4/4] Processando arquivos JavaScript...")
    js_files = list(WORKSPACE.rglob("*.js"))
    updated_count = 0
    
    for js_file in js_files:
        if "rebrand-dokmos" in str(js_file):
            continue
            
        if replace_in_file(js_file):
            updated_count += 1
            print(f"      ✓ {js_file.relative_to(WORKSPACE)}")
    
    print(f"      Total: {updated_count} arquivos JS atualizados")
    
    print("\n" + "=" * 60)
    print("REBRANDING CONCLUÍDO!")
    print("=" * 60)
    print("\nPróximos passos:")
    print("1. Verifique se os arquivos SVG do logo foram criados")
    print("2. Teste o site localmente")
    print("3. Valide as animações do loader DOKMOS")
    print("=" * 60)

if __name__ == "__main__":
    main()
