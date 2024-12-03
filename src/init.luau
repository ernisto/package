local wally = require(script.Config.wally)
local promise = require(script.Parent.promise)

export type cavalo = number
return table.freeze {
	promise = promise,
	wally = wally,
}
