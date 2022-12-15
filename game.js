const textElement = document.getElementById('text')
const optionButtonsElement =document.getElementById('option-buttons')

let state = {}

function startGame() {
  state = {}
  showTextNode(1)
}

function showTextNode(textNodeIndex) {
  const textNode = textNodes.find(textNode => textNode.id === textNodeIndex)
  textElement.innerText = textNode.text
  while (optionButtonsElement.firstChild) {
    optionButtonsElement.removeChild(optionButtonsElement.firstChild)
  }

  textNode.options.forEach(option => {
    if (showOption(option)) {
      const button = document.createElement('button')
      button.innerText = option.text
      button.classList.add('btn')
      button.addEventListener('click', () => selectOption(option))
      optionButtonsElement.appendChild(button)
    }
  })
}

function showOption(option) {
  return option.requiredState == null || option.requiredState(state)
}

function selectOption(option) {
    const nextTextNodeId = option.nextText
    if (nextTextNodeId <= 0) {
        return startGame()
    }
    state = Object.assign(state, option.setState)
    showTextNode(nextTextNodeId)
}

const textNodes = [
    {
        id: 1,
        text:'Welcome to Chemland! We have been waiting for you traveler!! This land has been cursed by the most' +
            ' evil of science... quantum mechanics, with the aid of his group, the theorist. Will take the conical flask and help free our land?',
        options: [
            {
                text: 'Yes, I will help',
                setState:{ConicalFlask: true},
                nextText: 2
            },
            {
                text:'No, I will not help',
                nextText: 4
            }
        ]
    },
    {
        id: 2,
        text: 'You carry on walking down a dark ally, a foe jumps in front of you. ' +
            'A battle stats...' +
            '(To kill the opponent you must get the answer right)' +
            'What property do wavelengths have? ',
        options: [
            {
                text: 'Wavelengths cannot be zero everywhere, or infinite anywhere ',
                nextText: 3
            },
            {
                text: 'Wavelengths can be zero everywhere',
                nextText: 4
            },
            {
                text: 'They are not continious',
                nextText: 4
            },
            {
                text: 'wavelengths are not real',
                nextText: 4
            }
        ]

    },
    {
        id: 4,
        text: "you got battered unlucky my slime",
        options:[
            {
                text: 'restart',
                nextText: -1
            },
        ]
    },
    {
        id: 7,
        text: 'Sorry traveler, this is incorrect! As reduced mass increases the ability of the molecule to rotate decrease as the moment of innertia is larger',
    },
    {
        id: 3,
        text: 'You beat the enemy and pick up a map.\n' +
            'You feel tired and need to recover from your battle, you find the nearest inn and sleep for the night' +
            'Do you survive the night?' +
            'Using Particle in the box theory, why doesn’t the' +
            '‘orbit’ of an electron around the proton in a hydrogen atom collapse so that the' +
            'electron comes into contact with the proton? ',
        options: [
            {
                text:' As the box gets larger the the translational energy increases becuase of the relationship between E and L',
                nextText: 4
            },
            {
                text: 'as you make the box smaller the translational energy goes up because there is an inverse relationship between E and the length of the box from',
                nextText: 5
            },
            {
                text: 'The paricle does not account for 3-D model, therefore the proton will have a higher energy than expected',
                nextText: 4
            }
        ]


    },
    {
        id: 5,
        text: 'Congratulations you survived teh night' +
            'you leave the inn and travel to a dark castle' +
            'you are greeted by a gard' +
            'hello traveler, to enter here a riddle must be answered' +
            'How does reduced mass effect vibrational frequency ',
        options: [
            {
                text: 'As reduced mass increases the vibrational frequency decreases, and as the reduced mass decreases the vibrational frequency increases ',
                nextText: 6
            },
            {
                text: 'As reduced mass increases the vibrational frequency increases, and as the reduced mass decreases the vibrational frequency decreases',
                nextText: 7
            },
            {

            }
        ]
    }

]

startGame()

if (typeof window !=='undifined') {
    console.log('you are on browser')
} else {
    consol.log('server')
}