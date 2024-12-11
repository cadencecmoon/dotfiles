vim.g.vimtex_compiler_method = 'latexmk'
vim.g.vimtex_compiler_latexmk = {
    out_dir = 'build',
    options = {
        '-xelatex',
        '-shell-escape',
        '-verbose',
        '-file-line-error',
        '-synctex=1',
        '-interaction=nonstopmode',
    },
}
vim.g.vimtex_view_method = 'zathura'

vim.g.tex_flavor = 'latex'
vim.g.vimtex_fold_manual = 1
