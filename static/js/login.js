particlesJS('particles-js', {
	// Configurações das partículas
	particles: {
		number: {
			value: 200, // Número de partículas
			density: {
				enable: true, // Habilita a densidade
				value_area: 800 // Área de densidade
			}
		},
		color: {
			value: '#008000' // Cor das partículas
		},
		shape: {
			type: 'circle', // Forma das partículas
			stroke: {
				width: 0, // Largura da linha das partículas
				color: '#000000' // Cor da linha das partículas
			},
			polygon: {
				nb_sides: 5 // Número de lados das partículas
			}
		},
		opacity: {
			value: 0.7, // Opacidade das partículas
			random: true, // Habilita a opacidade aleatória
			anim: {
				enable: true, // Habilita a animação de opacidade
				speed: 1, // Velocidade da animação de opacidade
				opacity_min: 0, // Opacidade mínima
				sync: false // Sincronização da animação de opacidade
			}
		},
		size: {
			value: 5, // Tamanho das partículas
			random: true, // Habilita o tamanho aleatório
			anim: {
				enable: false, // Habilita a animação de tamanho
				speed: 4, // Velocidade da animação de tamanho
				size_min: 0.3, // Tamanho mínimo
				sync: false // Sincronização da animação de tamanho
			}
		},
		line_linked: {
			enable: false, // Habilita o link de linha
			distance: 150, // Distância do link de linha
			color: '#ffffff', // Cor do link de linha
			opacity: 0.4, // Opacidade do link de linha
			width: 1 // Largura do link de linha
		},
		move: {
			enable: true, // Habilita o movimento das partículas
			speed: 1, // Velocidade do movimento das partículas
			direction: 'top', // Direção do movimento das partículas
			random: true, // Habilita a direção aleatória
			straight: false, // Habilita o movimento reto
			out_mode: 'out', // Modo de saída
			bounce: false, // Habilita o rebote
			attract: {
				enable: false, // Habilita a atração
				rotateX: 600, // Rotação no eixo X
				rotateY: 600 // Rotação no eixo Y
			}
		}
	},
	// Configurações de interatividade
	interactivity: {
		detect_on: 'canvas', // Detecção no canvas
		events: {
			onhover: {
				enable: true, // Habilita o evento de hover
				mode: 'repulse' // Modo do evento de hover
			},
			onclick: {
				enable: false, // Habilita o evento de clique
				mode: 'push' // Modo do evento de clique
			},
			resize: true // Habilita o redimensionamento
		},
		modes: {
			grab: {
				distance: 140, // Distância do modo de pegar
				line_linked: {
					opacity: 1 // Opacidade do link de linha no modo de pegar
				}
			},
			bubble: {
				distance: 400, // Distância do modo de bolha
				size: 40, // Tamanho do modo de bolha
				duration: 2, // Duração do modo de bolha
				opacity: 8, // Opacidade do modo de bolha
				speed: 3 // Velocidade do modo de bolha
			},
			repulse: {
				distance: 50, // Distância do modo de repulsão
				duration: 0.2 // Duração do modo de repulsão
			},
			push: {
				particles_nb: 25 // Número de partículas no modo de empurrar
			},
			remove: {
				particles_nb: 2 // Número de partículas no modo de remover
			}
		}
	  },
	  // Configurações de detecção de retina
	  retina_detect: true
	  });

const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

$(document).ready(function() {
	$('#signin-user').on('input', function() {
		$('#email-label').hide();
	});
  
	$('#signin-password').on('input', function() {
		$('#password-label').hide();
	});
  });
  
 