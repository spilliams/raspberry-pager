package main

import (
	"machine"

	"tinygo.org/x/drivers/st7789"
)

func main() {
	machine.I2C0.Configure(machine.I2CConfig{})
	screen := st7789.New(machine.I2C0)
	screen.Configure()
}
