var modal = document.getElementById("id_book-modal");
var btn = document.getElementById("id_book_modal_button");
var span = document.getElementsByClassName("close")[0];
var book_form = document.getElementById("id_book_modal_form")

// Modal de Livro

// Abrir modal
function OpenBookModal(title, author, synopsis, release_date, is_available) {
  modal.style.display = "block";
  book_form.innerHTML = `
    <div class="form-group">
      <form>
        <h1>Informações</h1>
        <ul>
          <li>
            <input type="text" name="title" maxlength="255" required="" id="id_title" value="${title}" readonly>
          </li>
          <li>
            <input type="text" name="author" maxlength="80" required="" id="id_author" value="${author}" readonly>
          </li>
          <li>
            <textarea name="synopsis" cols="40" rows="10" required="" id="id_synopsis" readonly>${synopsis}</textarea>
          </li>
          <li>
            <label for="id_release_date"><strong>Data de Lançamento:</strong> ${release_date}</label>
          </li>
          <li>
            <label for="id_is_available"><strong>Disponível</strong></label>
            <input type="checkbox" name="is_available" id="id_is_available" ${is_available ? 'checked' : ''} disabled>
          </li>
        </ul>
      </form>
    </div>
  `;
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