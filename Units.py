UnitConversions = {("meile", "mi"): { "kilometer" : 1.61, "feet" : 5280 },
                 ("kilometer", "km"): { "mile" : 0.621, "feet" : 3280 },
                 ("meter", "m"): { "inch" : 39.38, "feet" : 3.281 },
                 ("fuß","feet" "ft"): { "inch" : 12, "meter" : 0.305, "mile": 0.000189394},
                 ("inch", "zoll", "in"): { "feet" : 0.083, "meter": 0.0254}
                 }



UnitsFlat = d = {key: value for keys, value in UnitConversions.items() for key in keys}
