call scripts/wally-install.cmd model.project.json &

mkdir out\rojo &
rojo build model.project.json --output out/rojo/model.rbxm
