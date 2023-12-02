var modal = document.getElementById("id_book-modal");
var btn = document.getElementById("id_book_modal_button");
var span = document.getElementsByClassName("close")[0];
var book_form = document.getElementById("id_book_modal_form");

// Modal de Livro

// Abrir modal
function OpenBookModal(
  title,
  author,
  synopsis,
  genre,
  publisher,
  release_date,
  status,
  stock,
  id
) {
  modal.style.display = "block";
  book_form.innerHTML = `
    <div class="form-group">
      <form>
        <h1>Informações</h1>
        <ul>
        <li>
            <input type="text" name="title" maxlength="255" required="" id="id_title" value="${title}" readonly style="">
            <label for="title" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Título</label>
        </li>
        <li>
            <input type="text" name="author" maxlength="80" required="" id="id_author" value="${author}" readonly>
            <label for="author" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Autor</label>
        </li>
        <li>
            <textarea name="synopsis" cols="40" rows="10" required="" id="id_synopsis" readonly>${synopsis}</textarea>
            <label for="synopsis" style="margin-top: -210px; padding-left: 8px; color: #026948; font-weight: 500;">Sinópse</label>
        </li>
        <li>
            <input type="text" name="genre" maxlength="80" required="" id="id_genre" value="${genre}" readonly>
            <label for="author" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Gênero</label>
        </li>
        <li>
            <input type="text" name="publisher" maxlength="80" required="" id="id_publisher" value="${publisher}" readonly>
            <label for="author" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Editora</label>
        </li>   
        <li>
            <input type="text" name="author" maxlength="80" required="" id="id_author" value="${release_date}" readonly>
            <label for="author" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Data de Lançamento</label>
        </li>
        <li>
            <input type="text" name="author" maxlength="80" required="" id="id_author" value="${stock}" readonly>
            <label for="author" style="margin-top: -80px; padding-left: 8px; color: #026948; font-weight: 500;">Estoque</label>
        </li>
        </ul>
      </form>
    </div> 
      `;

  document.getElementById("book_id").value = id;
  document.getElementById("wishlist_add_book_id").value = id;
  document.getElementById("wishlist_remove_book_id").value = id;
  document.getElementById("edit_book_id").value = id;
}

// Fechar modal
span.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Filtragem de Livros

// Listener para as checkbox de filtragem
document
  .querySelectorAll('input[type="checkbox"]')
  .forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
      filterGalleries();
    });
  });

function filterGalleries() {
  // Obtém as checkbox
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');

  // Obgtem as galerias
  var galleries = document.querySelectorAll(".gallery");

  // Verifica se alguma checkbox está marcada
  var isAnyCheckboxChecked = Array.from(checkboxes).some(function (checkbox) {
    return checkbox.checked;
  });

  // Se nenhuma checkbox está marcada, exibe todas as galerias
  if (!isAnyCheckboxChecked) {
    galleries.forEach(function (gallery) {
      gallery.style.display = "flex";
    });
    return;
  }

  // Loop através de todas as galerias
  galleries.forEach(function (gallery) {
    // Obtém o tipo da galeria
    var galleryStatus = gallery.getAttribute("data-status");

    // Verificar se a galeria corresponde a algum dos filtros selecionados
    var matchesAnyFilter = Array.from(checkboxes).some(function (checkbox) {
      // Verifica se a checkbox está marcada e seu estado corresponde ao valor da checkbox
      if (checkbox.checked && checkbox.value === galleryStatus) {
        return true;
      }
      // Se não estiver marcada, ignora
      else {
        return false;
      }
    });

    // Se a galeria corresponde a algum dos filtros selecionados, exibir
    if (matchesAnyFilter) {
      gallery.style.display = "flex";
    }
    // Se não, esconder
    else {
      gallery.style.display = "none";
    }
  });
}

// Procura por livros

function filterBooks(searchQuery) {
  const books = document.querySelectorAll(".card");
  books.forEach(function (book) {
    const title = book
      .querySelector("button")
      .getAttribute("onclick")
      .split("'")[1];
    if (title.toLowerCase().includes(searchQuery.toLowerCase())) {
      book.style.display = "flex";
    } else {
      book.style.display = "none";
    }
  });
}

document.getElementById("search_button").addEventListener("click", function () {
  filterBooks(document.getElementById("search_input").value);
});

// ABRIR E FECHAR MODAL

const buttonClose = document.querySelector(".close")
const buttonClosea = document.querySelector(".closea")

const buttonLi = document.querySelector(".cad-li")
const modalLi = document.querySelector(".modal-li")

buttonLi.onclick = function (){
modalLi.show()
}

buttonClosea.onclick = function(){
modalLi.close()
}
