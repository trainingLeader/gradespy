import os
import moduloscustom.utilscustoms as uc
import moduloscustom.ui as ui
import moduloscustom.students as st
import moduloscustom.mensajes as msg
isAllow = True

if (__name__ == "__main__"):
    alumnos = []
    isAddStudent = True

    while (isAddStudent):
        os.system('cls')
        print(ui.menu)
        opcMenu = int(input(':)_'))
        match opcMenu:
            case 1:
                st.addStudent(alumnos)
            case 2:
                isViewGrade = True
                while (isViewGrade):
                    os.system('cls')
                    print(ui.menuNotas)
                    opcNota = int(input(':)'))
                    match opcNota:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            isViewGrade = uc.validateData(msg.messagemenugrade)
                        case _:
                            print('Pongase serio......Escriba bien....')
                            os.system('pause')
            case 3:
                isAddStudent = False
            case _:
                pass

                
