const cardControllers = document.querySelectorAll("[data-card-controller]");

//Botão que mostra informações do membro
cardControllers.forEach(controller => {
  controller.addEventListener("click", (e) => {
    const card = e.currentTarget.parentElement.parentElement;
    const isVisible = card.dataset.visible;

    //Ativa/desativa o conteúdo
    if (isVisible === "false") {
      card.setAttribute("data-visible", true);
    } else {
      card.setAttribute("data-visible", false);
    }
  })
})