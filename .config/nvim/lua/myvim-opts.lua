vim.cmd("set expandtab")
vim.cmd("set tabstop=2")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")
vim.cmd("set number")
vim.g.mapleader = " "

-- Mapeo para moverse entre ventanas con Ctrl + h/j/k/l
vim.api.nvim_set_keymap('n', '<C-k>', ':wincmd k<CR>', {silent = true})
vim.api.nvim_set_keymap('n', '<C-j>', ':wincmd j<CR>', {silent = true})
vim.api.nvim_set_keymap('n', '<C-h>', ':wincmd h<CR>', {silent = true})
vim.api.nvim_set_keymap('n', '<C-l>', ':wincmd l<CR>', {silent = true})

-- Mapeo para añadir un punto y coma al final de la línea en modo normal
vim.api.nvim_set_keymap('n', '<Leader>;', '$a;<Esc>', {silent = true})

-- Mapeo para guardar el archivo
vim.api.nvim_set_keymap('n', '<Leader>w', ':w<CR>', {silent = true})

-- Mapeo para salir del archivo
vim.api.nvim_set_keymap('n', '<Leader>q', ':q<CR>', {silent = true})



-- neotest 
-- Run current test
vim.api.nvim_set_keymap('n', '<Leader>rt', ':lua require("neotest").run.run()<CR>', {silent = true})

--stop current test
vim.api.nvim_set_keymap('n', '<Leader>rs', ':lua require("neotest").run.stop()<CR>', {silent = true})

-- open 
vim.api.nvim_set_keymap('n', '<Leader>ro', ':lua require("neotest").output.open()<CR>', {silent = true})

--info/summary test
vim.api.nvim_set_keymap('n', '<Leader>ri', ':lua require("neotest").summary.toggle()<CR>', {silent = true})

-- run all test in file
vim.api.nvim_set_keymap('n', '<Leader>rf', ':lua require("neotest").run.run(vim.fn.expand("%"))<CR>', {silent = true})
