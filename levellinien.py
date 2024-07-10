from pygame import draw

obere_begrenzung = [[14, 315], [261, 312], [261, 312], [264, 227], [264, 227], [45, 216], [45, 216], [58, 30], [58, 30], [610, 31], [614, 31], [614, 109], [614, 109], [667, 111], [667, 111], [671, 30], [671, 30], [1229, 34], [1229, 34], [1232, 217], [1232, 217], [1018, 223], [1018, 223], [1017, 314], [1013, 318], [1266, 316]]
untere_begrenzung = [[10, 357], [265, 358], [265, 358], [266, 452], [266, 450], [57, 457], [57, 457], [55, 558], [55, 558], [134, 562], [134, 562], [135, 583], [135, 583], [54, 588],[54, 588], [58, 690], [66, 688], [1226, 687], [1226, 687], [1230, 594], [1230, 594], [1154, 584], [1154, 584], [1150, 566], [1150, 566], [1227, 554], [1227, 554], [1230, 462], [1230, 462], [1020, 448], [1020, 448], [1014, 370], [1014, 360], [1262, 358]]
obere_innere_begrenzung = [[127, 184], [269, 184], [269, 184], [267, 156], [267, 156], [130, 150], [130, 150], [128, 182], [129, 114], [274, 112], [274, 112], [273, 62], [273, 62], [133, 62], [133, 62], [131, 110], [351, 111], [530, 112], [530, 112], [533, 68], [533, 68], [354, 63], [354, 63], [353, 112], [751, 114], [933, 112], [933, 112], [933, 65], [933, 65], [749, 63], [749, 63], [751, 113], [1016, 115], [1158, 114], [1158, 114], [1157, 68], [1157, 68], [1010, 65], [1010, 65], [1016, 114], [1018, 186], [1015, 156], [1015, 156], [1154, 153], [1154, 153], [1155, 187], [1155, 187], [1020, 186], [349, 323], [406, 318], [406, 318], [408, 257], [408, 257], [534, 250], [534, 250], [534, 222], [534, 222], [408, 218], [408, 218], [402, 154], [402, 154], [351, 152], [351, 152], [349, 314], [484, 182], [614, 187], [614, 187], [617, 246], [617, 246], [669, 247], [669, 247], [671, 185], [671, 185], [797, 184], [797, 184], [797, 154], [797, 154], [486, 154], [486, 154], [487, 182], [938, 317], [933, 157], [933, 157], [883, 153], [883, 153], [880, 218], [880, 218], [750, 221], [750, 221], [750, 252], [750, 252], [875, 254], [875, 254], [882, 314], [882, 314], [935, 312]] 
untere_innere_begrenzung = [[346, 358], [405, 356], [405, 358], [402, 452], [402, 452], [350, 450], [350, 450], [349, 362], [881, 361], [880, 450], [880, 450], [937, 450], [937, 450], [936, 358], [936, 358], [883, 358], [352, 495], [535, 494], [535, 494], [535, 518], [535, 522], [353, 521], [353, 521], [354, 495], [750, 492], [751, 521], [751, 521], [932, 518], [932, 518], [930, 494],[930, 494],[752, 492], [132, 492], [270, 493], [270, 493], [274, 586], [274, 586], [216, 588], [216, 588], [218, 525], [218, 525], [127, 522], [127, 522], [128, 492], [128, 492], [266, 489], [1012, 584], [1014, 497], [1014, 497], [1150, 493], [1150, 493], [1157, 524], [1157, 524], [1072, 526], [1072, 526], [1067, 580], [1067, 580], [1011, 584], [1011, 584], [1013, 498],[484, 425], [798, 426], [798, 426], [802, 454], [802, 454], [673, 456], [673, 456], [671, 518], [671, 518], [616, 522], [616, 522], [613, 458], [613, 458], [485, 454], [485, 454], [484, 430], [486, 559], [800, 558], [800, 558], [804, 590], [804, 590], [674, 594], [674, 594], [673, 651], [673, 651], [614, 653], [614, 653], [613, 593], [613, 593], [487, 590], [487, 590], [486, 563], [130, 654], [538, 654], [538, 654], [535, 627], [535, 627], [406, 624], [406, 624], [405, 561], [405, 561], [349, 558], [349, 558], [349, 620], [349, 620], [130, 630], [130, 630], [126, 654], [750, 654], [1153, 657], [1153, 657], [1150, 629], [1150, 629], [937, 625], [937, 625], [934, 565], [934, 565], [880, 562], [880, 562], [880, 620], [880, 620], [752, 626], [752, 626], [750, 653]]
geister_begrenzung = [[578, 305], [578, 293], [483, 293], [483, 293], [486, 383], [486, 383], [800, 382], [800, 382], [796, 294], [796, 294], [706, 293], [706, 293], [708, 302], [708, 302], [778, 304], [778, 304], [780, 372], [780, 372], [503, 374], [503, 374], [506, 302], [506, 302], [575, 302]]
farbe = (0,255,255)

def linien_malen(liste,gameDisplay):
    #obere begrenzung
    for i in range(0,len(liste)-1,2):
        draw.line(gameDisplay,farbe,(liste[i][0],liste[i][1]),(liste[i+1][0],liste[i+1][1]))

def levellininien_malen(gameDisplay):
    linien_malen(obere_begrenzung,gameDisplay)
    linien_malen(untere_begrenzung,gameDisplay)
    linien_malen(obere_innere_begrenzung,gameDisplay)
    linien_malen(untere_innere_begrenzung,gameDisplay)
    linien_malen(geister_begrenzung,gameDisplay)
