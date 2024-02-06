# .amh : ትንሽዬ, first language (stack based)

### Instructions list

    - PUSH (ግፋ): OPCODE NUM : push number to top of stack
    - POP (ንቀል): OPCODE: pop number from the stack and return it
    - ADD (ጨምር): OPCODE: pops 2 numbers from the stack and pushes there sum
    - SUB (ቀንስ): OPCODE: pops 2 numbers from the stack, subtracts the 1st from the 2nd
    - PRINT (ማተም): OPCODE STR_LITERAL: prints the string literal to the terminal
    - READ (አንብ): OPCODE : reads the number from IO input and pushes it to the stack
    - JUMP.EQ.0 (ዝለል.እኩ.0): OPCODE LABEL: jump to label if top of stack is 0
    - JUMP.GT.0 (ዝለል.ይበ.0): OPCODE LABEL: jump to label if top of stack is > 0
    - LOOP (ድገም)
    - LABEL (መለያ)
    - HALT (ተው)
