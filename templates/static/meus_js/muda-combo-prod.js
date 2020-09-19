(function () {
    ps = document.getElementById('produto_selecionado');

    ps.addEventListener('change', function () {
        preco_combo = this.options[this.selectedIndex].getAttribute('p_preco');
        desc_combo  = this.options[this.selectedIndex].getAttribute('p_desc');
        //window.alert(desc_combo);      
        document.getElementById('preco_selecionado').value = preco_combo;
        document.getElementById('desc_produto').value = desc_combo;

    })
})();

