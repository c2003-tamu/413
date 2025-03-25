import "elf"

rule preload {
  strings:
	$islib = /[a-zA-Z].so/
	$lshook = "readdir"
  condition:
	(elf.type == elf.ET_EXEC or elf.type == elf.ET_DYN) and ($islib and $lshook)
}
