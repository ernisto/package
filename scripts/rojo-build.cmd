call scripts/wally-install.cmd &
mkdir out\rojo &
rojo build dev.project.json --output out/rojo/game.rbxl
rojo build model.project.json --output out/rojo/package.rbxm