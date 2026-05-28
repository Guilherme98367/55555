#!/usr/bin/env python3
"""
Script de Validação do Rebranding DOKMOS
Verifica integridade de arquivos, caminhos de fontes e logos SVG.
"""

import os
import sys
from pathlib import Path

def check_file_exists(path, description):
    """Verifica se um arquivo existe e retorna status."""
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"  {status} {description}: {path}")
    return exists

def validate_rebrand():
    """Valida todo o rebranding DOKMOS."""
    print("=" * 60)
    print("VALIDAÇÃO DO REBRANDING DOKMOS")
    print("=" * 60)
    
    base_dir = Path("/workspace/rebrand-dokmos")
    all_passed = True
    
    # 1. Verificar estrutura de diretórios
    print("\n📁 Estrutura de Diretórios:")
    dirs_to_check = [
        base_dir / "logos",
        base_dir / "fonts/dokmos/regular",
        base_dir / "fonts/dokmos/medium",
        base_dir / "examples"
    ]
    
    for dir_path in dirs_to_check:
        exists = dir_path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {dir_path.name}: {dir_path}")
        if not exists:
            all_passed = False
    
    # 2. Verificar arquivos de logo SVG
    print("\n🎨 Logos SVG:")
    logos = [
        (base_dir / "logos" / "dokmos-logo-primary.svg", "Logo Primária"),
        (base_dir / "logos" / "dokmos-logo-white.svg", "Logo Branca"),
        (base_dir / "logos" / "dokmos-icon.svg", "Ícone"),
        (base_dir / "logos" / "dokmos-loader-paths.svg", "Loader Paths")
    ]
    
    for logo_path, desc in logos:
        if not check_file_exists(logo_path, desc):
            all_passed = False
    
    # 3. Verificar arquivos de fonte
    print("\n🔤 Fontes Dokmos:")
    fonts = [
        (base_dir / "fonts/dokmos/regular/dokmos-Regular.ttf", "Regular TTF"),
        (base_dir / "fonts/dokmos/regular/dokmos-Regular.woff", "Regular WOFF"),
        (base_dir / "fonts/dokmos/regular/dokmos-Regular.woff2", "Regular WOFF2"),
        (base_dir / "fonts/dokmos/medium/dokmos-Medium.ttf", "Medium TTF"),
        (base_dir / "fonts/dokmos/medium/dokmos-Medium.woff", "Medium WOFF"),
        (base_dir / "fonts/dokmos/medium/dokmos-Medium.woff2", "Medium WOFF2")
    ]
    
    for font_path, desc in fonts:
        if not check_file_exists(font_path, desc):
            all_passed = False
    
    # 4. Verificar CSS de fontes
    print("\n🎨 CSS de Fontes:")
    css_path = base_dir / "fonts/dokmos/dokmos-fonts.css"
    if not check_file_exists(css_path, "DOKMOS Fonts CSS"):
        all_passed = False
    else:
        # Verificar conteúdo do CSS
        with open(css_path, 'r') as f:
            content = f.read()
            if "font-family: 'Dokmos'" in content:
                print("  ✓ Font-family 'Dokmos' definida corretamente")
            else:
                print("  ✗ Font-family 'Dokmos' não encontrada no CSS")
                all_passed = False
    
    # 5. Verificar exemplo HTML
    print("\n📄 Exemplo HTML:")
    example_path = base_dir / "examples/demo-dokmos.html"
    if not check_file_exists(example_path, "Demo DOKMOS"):
        all_passed = False
    else:
        with open(example_path, 'r') as f:
            content = f.read()
            checks = [
                ("DOKMOS" in content, "Menções a DOKMOS"),
                ("dokmos" in content.lower(), "Referências lowercase dokmos"),
                ("#286875" in content, "Cor primária Teal"),
                ("D-O-K-M-O-S" in content or "path" in content, "Paths do loader")
            ]
            for passed, desc in checks:
                status = "✓" if passed else "✗"
                print(f"  {status} {desc}")
                if not passed:
                    all_passed = False
    
    # 6. Verificar conteúdo dos SVGs
    print("\n🔍 Validação de Conteúdo SVG:")
    svg_files = [
        (base_dir / "logos/dokmos-logo-primary.svg", ["#286875", "DOKMOS"]),
        (base_dir / "logos/dokmos-icon.svg", ["rect", "rx="])
    ]
    
    for svg_path, required_strings in svg_files:
        if svg_path.exists():
            with open(svg_path, 'r') as f:
                content = f.read()
                for req_str in required_strings:
                    if req_str in content:
                        print(f"  ✓ {svg_path.name} contém '{req_str}'")
                    else:
                        print(f"  ✗ {svg_path.name} NÃO contém '{req_str}'")
                        all_passed = False
    
    # Resultado final
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ VALIDAÇÃO CONCLUÍDA COM SUCESSO!")
        print("Todos os arquivos do rebranding DOKMOS estão presentes e corretos.")
    else:
        print("❌ VALIDAÇÃO FALHOU!")
        print("Alguns arquivos ou configurações estão incorretos.")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(validate_rebrand())
