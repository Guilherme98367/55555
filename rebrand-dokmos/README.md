# 🎨 Rebranding DOKMOS - Pacote Completo

Este diretório contém todos os assets e arquivos necessários para o rebranding de **TROA/TR3A** para **DOKMOS**.

---

## 📁 Estrutura de Arquivos

```
rebrand-dokmos/
├── logos/                          # Logotipos vetoriais SVG
│   ├── dokmos-logo-primary.svg     # Logo completa (símbolo + texto) - Cor primária
│   ├── dokmos-logo-white.svg       # Logo completa - Versão branca (fundos escuros)
│   ├── dokmos-icon.svg             # Símbolo isolado (favicon, avatar)
│   └── dokmos-loader-paths.svg     # Paths individuais para animação do loader
│
├── fonts/dokmos/                   # Fonte Dokmos (renomeada de TR3A)
│   ├── dokmos-fonts.css            # Definições @font-face
│   ├── regular/
│   │   ├── dokmos-Regular.ttf
│   │   ├── dokmos-Regular.woff
│   │   └── dokmos-Regular.woff2
│   └── medium/
│       ├── dokmos-Medium.ttf
│       ├── dokmos-Medium.woff
│       └── dokmos-Medium.woff2
│
├── examples/
│   └── demo-dokmos.html            # Página de demonstração completa
│
└── validate_rebrand.py             # Script de validação automática
```

---

## 🎯 Identidade Visual DOKMOS

### Cores da Marca
| Cor | Hex | Uso |
|-----|-----|-----|
| **Primária** | `#286875` | Teal/Blue-green - cor principal |
| **Primária Light** | `#3d8a99` | Variação mais clara |
| **Branco** | `#FFFFFF` | Elementos em fundos escuros |
| **Dark** | `#1a4a55` | Textos e detalhes |

### Símbolo
- **4 barras verticais arredondadas** em arranjo interleaved
- Representação estilizada minimalista (conceito WM/DOKMOS)
- Cantos arredondados (rx=7 ou rx=8)
- Proporção 1:1 para ícone

### Tipografia
- **Fonte principal:** Dokmos (renomeada de TR3A)
- **Fontes fallback:** Montserrat, Outfit, Helvetica Neue, Arial
- **Pesos:** Regular (400) e Medium (500)

---

## 🚀 Como Implementar no Site Existente

### Passo 1: Copiar Fontes
```bash
# Copiar estrutura de fontes para o site
cp -r /workspace/rebrand-dokmos/fonts/dokmos /workspace/ativos/fonts/
```

### Passo 2: Atualizar CSS de Fontes
Substituir as definições `@font-face` no CSS principal:
```css
/* ANTES (TR3A) */
@font-face {
  font-family: 'TR3A';
  src: url('../fonts/tr3a/regular/tr3a-Regular.woff2') format('woff2');
}

/* DEPOIS (DOKMOS) */
@font-family: 'Dokmos';
src: url('../fonts/dokmos/regular/dokmos-Regular.woff2') format('woff2');
```

### Passo 3: Substituir Logo SVG
Localizar todos os `<symbol id="icon-logo">` ou logos inline e substituir pelo conteúdo de:
- `logos/dokmos-logo-primary.svg` (modo claro)
- `logos/dokmos-logo-white.svg` (modo escuro)
- `logos/dokmos-icon.svg` (favicon, avatar)

### Passo 4: Atualizar Loader
No HTML principal, substituir a animação do loader:
```html
<!-- ANTES (TROA - 4 letras) -->
<path d="[T]" style="--delay: 0.3s;"></path>
<path d="[R]" style="--delay: 0.225s;"></path>
<path d="[O]" style="--delay: 0.15s;"></path>
<path d="[A]" style="--delay: 0.075s;"></path>

<!-- DEPOIS (DOKMOS - 6 letras) -->
<path d="[D]" style="--delay: 0.35s;"></path>
<path d="[O]" style="--delay: 0.28s;"></path>
<path d="[K]" style="--delay: 0.21s;"></path>
<path d="[M]" style="--delay: 0.14s;"></path>
<path d="[O]" style="--delay: 0.07s;"></path>
<path d="[S]" style="--delay: 0s;"></path>
```

### Passo 5: Atualizar Metadados e Textos
- `<title>`: Trocar "Troa" por "Dokmos"
- Meta descriptions
- Rodapés e créditos
- Alt texts de imagens

---

## ✅ Validação

Execute o script de validação:
```bash
python3 /workspace/rebrand-dokmos/validate_rebrand.py
```

Saída esperada:
```
✅ VALIDAÇÃO CONCLUÍDA COM SUCESSO!
Todos os arquivos do rebranding DOKMOS estão presentes e corretos.
```

---

## 🧪 Teste Local

Abra o arquivo de demonstração no navegador:
```bash
# Iniciar servidor HTTP simples
cd /workspace/rebrand-dokmos/examples
python3 -m http.server 8080

# Acessar: http://localhost:8080/demo-dokmos.html
```

Verifique:
1. ✅ Animação do loader com D-O-K-M-O-S (6 letras)
2. ✅ Logo com barras verticais arredondadas
3. ✅ Cor teal (#286875) aplicada corretamente
4. ✅ Fonte Dokmos carregando sem erros

---

## 📋 Checklist de Implementação

- [ ] Copiar pasta `fonts/dokmos/` para `ativos/fonts/`
- [ ] Renomear/sobrescrever pasta `tr3a/` existente
- [ ] Atualizar `@font-face` em todos os CSS/HTML
- [ ] Substituir logo SVG no header
- [ ] Atualizar animação do loader (6 paths)
- [ ] Alterar `<title>` e meta tags
- [ ] Atualizar rodapé e créditos
- [ ] Testar em múltiplos navegadores
- [ ] Validar com script `validate_rebrand.py`

---

## 📄 Licença

Assets criados para uso exclusivo no projeto DOKMOS.

---

**Criado em:** Maio 2024  
**Versão:** 1.0  
**Status:** ✅ Validado
