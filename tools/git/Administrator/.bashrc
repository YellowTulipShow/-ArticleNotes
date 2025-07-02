alias git_allpush='git add . && git commit -m "change new content" && git push origin master'

# 为 git sync-ignore 添加分支名补全
_git_sync_ignore() {
    # 获取所有本地分支
    local branches="$(git for-each-ref --format='%(refname:short)' refs/heads/)"

    # 设置补全选项
    COMPREPLY=($(compgen -W "$branches" -- "${COMP_WORDS[COMP_CWORD]}"))
}

# 注册补全函数
if declare -f _git >/dev/null; then
    _git_sync_ignore() {
        _git_sync_ignore
    }
    # 确保在 Git 命令补全中识别这个子命令
    __git_complete git _git_sync_ignore
    __git_complete git sync-ignore _git_sync_ignore
fi
