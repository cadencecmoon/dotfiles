--local present, tree_c = pcall(require, "nvim-tree.config")
--if not present then
--    return
--end

local g = vim.g

g.nvim_tree_side = "left"
g.nvim_tree_width = 25
g.nvim_tree_auto_ignore_ft = {"dashboard"} -- don't open tree on specific fiypes.
g.nvim_tree_allow_resize = 1

require "mappings".nvimtree()

require'nvim-tree'.setup{
    disable_netrw       = true,
    hijack_netrw        = true,
    --open_on_setup       = false,
    --ignore_ft_on_setup  = {},
    open_on_tab         = false,
    hijack_cursor       = false,
    update_cwd          = false,
    renderer = {
        add_trailing = false,
        highlight_opened_files = "none",
        highlight_git = true,
        root_folder_modifier = table.concat {":t:gs?$?/..", string.rep(" ", 1000), "?:gs?^??"},
        indent_markers = {
            enable = true,
        },
        icons = {
            show = {
                git = true,
                folder = true,
                file = true,
            },
            glyphs = {
                default = "",
                symlink = "",
                git = {
                    unstaged = "✗",
                    staged = "✓",
                    unmerged = "",
                    renamed = "➜",
                    untracked = "★",
                    deleted = "",
                    ignored = "◌"
                },
                folder = {
                    arrow_open = "",
                    arrow_closed = "",
                    default = "",
                    open = "",
                    empty = "", -- 
                    empty_open = "",
                    symlink = "",
                    symlink_open = ""
                },
            },
        },
    },
    update_focused_file = {
        enable      = false,
        update_cwd  = false,
        ignore_list = {}
    },
    system_open = {
        cmd  = nil,
        args = {}
    },
    view = {
        width = 30,
        side = 'left'
    },
    actions = {
        open_file = {
            resize_window = false,
            quit_on_open = false,
        }
    }
}
