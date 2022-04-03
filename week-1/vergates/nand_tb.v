`include "nand_gate.v"
module nand_tb;
  reg a;
  reg b;
  wire y;

  nand_gate uut(
    .a(a),
    .b(b),
    .y(y)
  );

  initial begin
    a = 0;
    b = 0;
    $dumpfile("signals.vcd");
    $dumpvars(0, nand_tb);
    #3000;
    $finish();
  end
endmodule

