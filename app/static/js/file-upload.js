document.getElementById('select-file')
    .addEventListener('click', () => document.getElementById('selected-file').click(), false);

document.getElementById('selected-file').onchange = () => {
    const fileData = $('#selected-file').prop('files')[0];
    const formData = new FormData();

    formData.append('file', fileData);

    $.ajax({
      url: '/importar',
      type: 'POST',
      cache: false,
      processData: false,
      contentType: false,
      dataType : 'json',
      data: formData,
      success: () => console.log("Arquivo importado com sucesso.")
    });
};
