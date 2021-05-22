import copy

ascii_nums = {
     0: ["   ",
         "XXX",
         "X X",
         "X X",
         "X X",
         "XXX",
         "   "],
    1: ["   ",
        " X ",
        "XX ",
        " X ",
        " X ",
        "XXX",
        "   "],
    2: ["   ",
        "XXX",
        "  X",
        "XXX",
        "X  ",
        "XXX",
        "   "],
      3: ["   ",
          "XXX",
          "  X",
          "XXX",
          "  X",
          "XXX",
          "   "],
     4: ["   ",
         "X X",
         "X X",
         "XXX",
         "  X",
         "  X",
         "   "],
      5: ["   ",
          "XXX",
          "X  ",
          "XXX",
          "  X",
          "XXX",
          "   "],
      6: ["   ",
          "XXX",
          "X  ",
          "XXX",
          "X X",
          "XXX",
          "   "]
}

DASH=["    ",
      "    ",
      "    ",
      " XX ",
      "    ",
      "    ",
      "    "]

LETTERW=["     ",
         "X   X",
         "X   X",
         "X   X",
         "X X X",
         "XXXXX",
         "     "]

LETTERI=["   ",
         "XXX",
         " X ",
         " X ",
         " X ",
         "XXX",
         "   "]

LETTERN=["    ",
         "X  X",
         "XX X",
         "X XX",
         "X  X",
         "X  X",
         "    "]

PUNCEXCALM=["  ",
            "X ",
            "X ",
            "X ",
            "  ",
            "X ",
            "  "]

#Create dictionaries to store scoring numbers/text
scoredict = copy.deepcopy(ascii_nums)
scoredict["dash"] = DASH
textdict={"W":LETTERW,"I":LETTERI,"N":LETTERN,"!":PUNCEXCALM}
