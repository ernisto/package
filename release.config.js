const config = {
    branches: ['master'],
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        ['@semantic-release/git', {
            assets: ["out/rojo/model.rbxm"],
            message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
        }],
        ["@semantic-release/github", {
            assets: [
                { path: "out/rojo/model.rbxm", label: "Rojo build" },
            ]
        }],
        ["@semantic-release/exec", {
            prepareCmd: "shell scripts/release ${nextRelease.version}",
            publishCmd: "wally publish"
        }]
    ]
}

module.exports = config
