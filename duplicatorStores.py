from pathlib import Path

destino = Path.cwd() / 'src' / 'stores'

if not section4.exists():
    print('no existe section4')
    exit()

pathQuestionModel = Path.cwd() / 'src' / 'components' / 'section4' / 'Q_4_1' / 'Q_4_1.vue'
if not pathQuestionModel.exists():
    print('no existe pathQuestionModel')
    exit()

pathSystemCardModel = Path.cwd() / 'src' / 'components' / 'section4' / 'Q_4_1' / 'system_card_A.vue'
if not pathSystemCardModel.exists():
    print('no existe pathSystemCardModel')
    exit()

questionModel = pathQuestionModel.read_text()
systemCardModel = pathSystemCardModel.read_text()

name = 'Q_4_'

oldPlace = 'Q_4_1'

for x in range(2, 18):
    if x == 3:
        continue
    newPlace = name + str(x)
    pathDir = section4 / newPlace
    if not pathDir.exists():
        pathDir.mkdir()
    print('pathDir', pathDir)
    questionContent = questionModel.replace(oldPlace, newPlace).replace('IIDD',f'4.{x}')
    pathQuestion = pathDir / f'{newPlace}.vue'
    pathQuestion.write_text(questionContent)
    print('pathQuestion', pathQuestion)
    pathSystem = pathDir / 'system_card_A.vue'
    pathSystem.write_text(systemCardModel)
    print('pathSystem', pathSystem)


