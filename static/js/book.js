var modal = document.getElementById("id_book-modal");
var btn = document.getElementById("id_book_modal_button");
var span = document.getElementsByClassName("close")[0];
var book_form = document.getElementById("id_book_modal_form")

// Modal de Livro

// Abrir modal
function OpenBookModal(title, author, synopsis, genre, publisher, release_date, status, stock, id) {
  modal.style.display = "block"; 
  book_form.innerHTML = `
    <div class="form-group">
      <form>
        <h1>Informações</h1>
        <ul>
        <li>
            <label id="id_title"><strong>Título:</strong> ${title}</label>
        </li>
        <li>
            <label id="id_author"><strong>Autor:</strong> ${author}</label>
        </li>
        <li>
            <label id="id_synopsis"><strong>Sinópse:</strong> ${synopsis}</label>
        </li>
        <li>
            <label id="id_genre"><strong>Gênero:</strong> ${genre}</label>
        </li>    
        <li>
            <label id="id_publisher"><strong>Editora:</strong> ${publisher}</label>
        </li>    
        <li>
            <label for="id_release_date"><strong>Data de Lançamento:</strong> ${release_date}</label>
        </li>
        <li>
            <label for="id_status"><strong>Disponibilidade:</strong> ${status}</label>
        </li>
        <li>
            <label for="id_stock"><strong>Estoque:</strong> ${stock}</label>
        </li>
        </ul>
      </form>
      </div> 
      `;

      document.getElementById('book_id').value = id;
      document.getElementById('wishlist_add_book_id').value = id;
      document.getElementById('wishlist_remove_book_id').value = id;
      document.getElementById('edit_book_id').value = id;
}

// Fechar modal
span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Filtragem de Livros

// Listener para as checkbox de filtragem
document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
  checkbox.addEventListener('change', function() {
      filterGalleries();
  });
});

function filterGalleries() {
  // Obtém as checkbox
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');

  // Obgtem as galerias
  var galleries = document.querySelectorAll('.gallery');

  // Verifica se alguma checkbox está marcada
  var isAnyCheckboxChecked = Array.from(checkboxes).some(function(checkbox) {
    return checkbox.checked;
  });

  // Se nenhuma checkbox está marcada, exibe todas as galerias
  if (!isAnyCheckboxChecked) {
    galleries.forEach(function(gallery) {
      gallery.style.display = 'flex';
    });
    return;
  }

  // Loop através de todas as galerias
  galleries.forEach(function(gallery) {
    // Obtém o tipo da galeria
    var galleryStatus = gallery.getAttribute('data-status');

    // Verificar se a galeria corresponde a algum dos filtros selecionados
    var matchesAnyFilter = Array.from(checkboxes).some(function(checkbox) {
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
      gallery.style.display = 'flex';
    }
    // Se não, esconder
    else {
      gallery.style.display = 'none';
    }
  });
}