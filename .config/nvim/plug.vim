if has("nvim")
  let g:plug_home = stdpath('data') . '/plugged'
endif

call plug#begin()

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'

if has("nvim")
  "LUALINE"
  Plug 'hoob3rt/lualine.nvim'

  "DEFX"
  Plug 'kristijanhusak/defx-git'
  Plug 'kristijanhusak/defx-icons'
  "Plug 'preservim/nerdtree'
  "Plug 'Xuyuanp/nerdtree-git-plugin'
  "Plug 'ryanoasis/vim-devicons'
  "Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
  Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' }

  "LSP Config"
  Plug 'neovim/nvim-lspconfig'
  Plug 'williamboman/nvim-lsp-installer'
  Plug 'tami5/lspsaga.nvim'
  Plug 'folke/lsp-colors.nvim'

  "LUASNIP + CMP"
  Plug 'L3MON4D3/LuaSnip'
  Plug 'hrsh7th/cmp-nvim-lsp'
  Plug 'hrsh7th/cmp-buffer'
  Plug 'hrsh7th/cmp-path'
  Plug 'hrsh7th/cmp-cmdline'
  Plug 'hrsh7th/nvim-cmp'
  Plug 'saadparwaiz1/cmp_luasnip'

  "treesitter for fuzzy
  Plug 'nvim-treesitter/nvim-treesitter', { 'do': ':TSUpdate' }
  Plug 'nvim-telescope/telescope.nvim'
  Plug 'kyazdani42/nvim-web-devicons'

  Plug 'onsails/lspkind-nvim'
  Plug 'nvim-lua/popup.nvim'
  Plug 'nvim-lua/plenary.nvim'

  Plug 'windwp/nvim-autopairs'
  Plug 'windwp/nvim-ts-autotag'
  Plug 'scrooloose/nerdcommenter'
  Plug 'rafamadriz/friendly-snippets'

  Plug 'lumiliet/vim-twig'
endif

Plug 'groenewege/vim-less', { 'for': 'less' }
Plug 'kchmck/vim-coffee-script', { 'for': 'coffee' }

call plug#end()

