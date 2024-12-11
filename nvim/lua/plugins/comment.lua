local present, nvim_comment = pcall(require, "nvim_comment")
if present then
    nvim_comment.setup({comment_empty = false})
end

