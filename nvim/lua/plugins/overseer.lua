require("overseer").setup()

local overseer = require('overseer')

overseer.register_template({
    name = "lilypond",
    builder = function(params)
        return {
            cmd = {"lilypond", vim.fn.expand("%:p:t")},
            name = "lilypond",
            cwd = "",
            env = {},
            components = {
                "default"
            },
            metadata = {},
        }
    end,
    desc = "Compile lilypond file",
    tags = {overseer.TAG.BUILD},
    params = {},
    priority = 50,
    condition = {
        filetype = {"lilypond"},
    },
})
