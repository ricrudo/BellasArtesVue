from pathlib import Path
import re

key1 = '</h3>'

icono = '''<span
        v-if="popupText !== ''"
        class="info-icon"
        @click="popupToggleShow">
        ℹ️
      </span>
    </h3>'''

newProp = ''',
    popupText: {
      type:String,
      required:false,
    }
})


  const popupState = ref(false)

  function popupToggleShow() {
    popupState.value = !popupState.value
  }

'''

cuadro_texto = '''
        <div class="popup" v-if="popupText !== ''" v-show="popupState">
          <span
              class="close-btn"
              @click="popupToggleShow">
            &times;
          </span>
          <p>{{popupText}}</p>
        </div>
'''


root = Path.cwd() / 'src' / 'components' / 'elements'

for archivo in root.iterdir():
    if not archivo.name.startswith(".") and archivo.suffix == ".vue":
        content = archivo.read_text()
        if 'form-item' in content and content.count(key1) == 1 and not 'popupState' in content:
            content = content.replace(key1, icono)
            match = re.search(r'(.*)\}\)(.*)', content, flags=re.DOTALL)
            if match:
                content = match.groups()[0] + newProp + match.groups()[1]
                match = re.search(r'(.*)(</div>.*)', content, flags=re.DOTALL)
                if match:
                    content = match.groups()[0] + cuadro_texto + match.groups()[1]
                    print(archivo)
                    archivo.write_text(content)
