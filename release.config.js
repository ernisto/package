const config = {
    branches: ['master'],
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        ['@semantic-release/git', {
            assets: ["out/rojo/game.rbxl"],
            message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
        }],
        ["@semantic-release/github", {
            assets: [
                { path: "out/rojo/game.rbxl", label: "Rojo build" },
            ]
        }],
        ["@semantic-release/exec", {
            prepareCmd: "python scripts/python/set-wally-version.py ./wally.toml ${nextRelease.version}",
            publishCmd: "wally publish"
        }]
    ]
}

module.exports = config
