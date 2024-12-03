local wally = require(script.Config.wally)
local promise = require(script.Parent.promise)
return table.freeze {
	promise = promise,
	wally = wally,
}
