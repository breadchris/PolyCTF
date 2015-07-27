syntax on
set t_Co=256

map <TAB> >gv
map <S-TAB> <gv
map <Enter> i<Enter>

cmap w!! w !sudo tee %

set laststatus=2
set number
set cursorline 
set ruler
set mouse=a

" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" Ignore case when searching
set ignorecase

" When searching try to be smart about cases 
set smartcase

set nobackup
set nowb
set noswapfile

set expandtab
set shiftwidth=4
set tabstop=4

" Vim color scheme
"
" Name:        railscast.vim
" Maintainer:  Josh O'Rourke <joshorourke@me.com>
" License:     public domain
"
" A GUI Only port of the RailsCasts TextMate theme [1] to Vim.
" Some parts of this theme were borrowed from the well-documented Lucius theme [2].
"
" [1] http://railscasts.com/about
" [2] http://www.vim.org/scripts/script.php?script_id=2536

set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "railscasts"

" Colors
" Brown        #BC9458
" Dark Blue    #6D9CBE
" Dark Green   #519F50
" Dark Orange  #CC7833
" Light Blue   #D0D0FF
" Light Green  #A5C261
" Tan          #FFC66D

hi Normal                    guifg=#E6E1DC guibg=#2B2B2B ctermfg=white ctermbg=234
hi Cursor                    guifg=#000000 guibg=#FFFFFF ctermfg=0 ctermbg=15   
hi CursorLine                guibg=#333435 ctermbg=235 cterm=NONE
hi Search                    guibg=#5A647E ctermfg=NONE ctermbg=236 cterm=underline
hi Visual                    guibg=#5A647E ctermbg=60
hi LineNr                    guifg=#888888 ctermfg=242
hi StatusLine                guibg=#414243 gui=NONE guifg=#E6E1DC
hi StatusLineNC              guibg=#414243 gui=NONE
hi VertSplit                 guibg=#414243 gui=NONE guifg=#414243
hi CursorLineNr              guifg=#bbbbbb ctermfg=248
hi ColorColumn               guibg=#333435 ctermbg=235

" Folds
" -----
" line used for closed folds
hi Folded                    guifg=#F6F3E8 guibg=#444444 gui=NONE

" Invisible Characters
" ------------------
hi NonText                   guifg=#777777 gui=NONE
hi SpecialKey                guifg=#777777 gui=NONE

" Misc
" ----
" directory names and other special names in listings
hi Directory                 guifg=#A5C261 gui=NONE

" Popup Menu
" ----------
" normal item in popup
hi Pmenu                     guifg=#F6F3E8 guibg=#444444 gui=NONE
" selected item in popup
hi PmenuSel                  guifg=#000000 guibg=#A5C261 gui=NONE
" scrollbar in popup
hi PMenuSbar                 guibg=#5A647E gui=NONE
" thumb of the scrollbar in the popup
hi PMenuThumb                guibg=#AAAAAA gui=NONE


"rubyComment
hi Comment                   guifg=#BC9458 gui=italic ctermfg=137
hi Todo                      guifg=#BC9458 guibg=NONE gui=italic ctermfg=94

"rubyPseudoVariable
"nil, self, symbols, etc
hi Constant                  guifg=#6D9CBE ctermfg=73

"rubyClass, rubyModule, rubyDefine
"def, end, include, etc
hi Define                    guifg=#CC7833 ctermfg=173

"rubyInterpolation
hi Delimiter                 guifg=#519F50

"rubyError, rubyInvalidVariable
hi Error                     guifg=#FFFFFF guibg=#990000 ctermfg=221 ctermbg=88

"rubyFunction
hi Function                  guifg=#FFC66D gui=NONE ctermfg=221 cterm=NONE

"rubyIdentifier
"@var, @@var, $var, etc
hi Identifier                guifg=#D0D0FF gui=NONE ctermfg=73 cterm=NONE

"rubyInclude
"include, autoload, extend, load, require
hi Include                   guifg=#CC7833 gui=NONE ctermfg=173 cterm=NONE

"rubyKeyword, rubyKeywordAsMethod
"alias, undef, super, yield, callcc, caller, lambda, proc
hi Keyword                   guifg=#CC7833 ctermfg=172 cterm=NONE

" same as define
hi Macro                     guifg=#CC7833 gui=NONE ctermfg=172

"rubyInteger
hi Number                    guifg=#A5C261 ctermfg=107

" #if, #else, #endif
hi PreCondit                 guifg=#CC7833 gui=NONE ctermfg=172 cterm=NONE

" generic preprocessor
hi PreProc                   guifg=#CC7833 gui=NONE ctermfg=103

"rubyControl, rubyAccess, rubyEval
"case, begin, do, for, if unless, while, until else, etc.
hi Statement                 guifg=#CC7833 gui=NONE ctermfg=172 cterm=NONE

"rubyString
hi String                    guifg=#A5C261 ctermfg=107

hi Title                     guifg=#FFFFFF ctermfg=15

"rubyConstant
hi Type                      guifg=#DA4939 gui=NONE

hi DiffAdd                   guifg=#E6E1DC guibg=#144212
hi DiffDelete                guifg=#E6E1DC guibg=#660000

hi link htmlTag              xmlTag
hi link htmlTagName          xmlTagName
hi link htmlEndTag           xmlEndTag

hi xmlTag                    guifg=#E8BF6A
hi xmlTagName                guifg=#E8BF6A
hi xmlEndTag                 guifg=#E8BF6A


set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Bundle 'gmarik/vundle'
Bundle 'The-NERD-tree'
Bundle 'php.vim-for-php5'
Bundle 'SuperTab-continued.'
Bundle 'TagHighlight'
Bundle 'https://github.com/scrooloose/syntastic.git'
Bundle 'lsdr/monokai'
 
call vundle#end()
filetype plugin on

let mapleader = ","
let g:mapleader = ","

set hidden "Allow unsaved files to be hidden

"Turn off backup since everything is tracked in version control
set nobackup
set nowb
set noswapfile
"

set statusline=%F%m%r%h%w[%L][%{&ff}]%y[%p%%][%l,%v]
"              | | | | |  |   |      |  |     |  |
"              | | | | |  |   |      |  |     |  +- current col
"              | | | | |  |   |      |  |     +- current line
"              | | | | |  |   |      |  +- cur percent of file
"              | | | | |  |   |      +- cur syntax
"              | | | | |  |   +- cur fileformat
"              | | | | |  +- num lines
"              | | | | +- preview flag
"              | | | +- help flag
"              | | +- readonly flag
"              | +- modified flag
"              +- full path to file

set ttyfast "Assume a fast connection
set nu
set backspace=indent,eol,start
set wildmenu                   "show list instead of just completing
set wildignore=*.dll,*.o,*.obj,*.bak,*.exe,*.pyc,*.jpg,*.gif,*.png,*.cml
set wildmode=list:longest,full "completion: list matches, longest common part, then all
set scrolljump=5               "lines to scroll when cursor leaves screen
set scrolloff=3                "minlines to keep above and below cursor
set showmatch
set hlsearch
set incsearch
set ignorecase
set smartcase

set autoindent
set shiftwidth=4
set tabstop=4
set expandtab
set smarttab
set noswapfile

"Use the PHP doc program to lookup things in <normal>K press
autocmd FileType php set keywordprg=pman

" Remaps {
    " make moving thorugh windows easier
    map <C-j> <C-w>j
    map <C-k> <C-w>k
    map <C-h> <C-w>h
    map <C-l> <C-w>l
 
    "Treat long lines as break lines
    map j gj
    map k gk
 
    imap jj <esc>
    map ; :
    map <leader>f <Esc>:NERDTreeToggle<CR>
"}

" Specific PHP settings {
let g:php_sql_query = 1
let g:php_special_vars = 1
let g:php_special_functions = 1
let g:php_smart_semicolon = 1
" }
iabbrev </ </<C-X><C-O>

let g:syntastic_cpp_compiler_options = '-std=c++11'

