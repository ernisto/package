call scripts/wally-install.cmd &
mkdir out\rojo &

echo --!nocheck> Packages/init.luau
echo return require(script.package) >> Packages/init.luau

rojo build dev.project.json --output out/rojo/game.rbxl
rojo build model.project.json --output out/rojo/model.rbxm