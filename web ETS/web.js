// Ambil elemen tombol dan tabel
const tombol = document.getElementById("tombolTampilWisata");
const tabel = document.getElementById("daftarWisata");

// Tambahkan event listener untuk tombol
tombol.addEventListener("click", async function() {
    // Kirim permintaan ke API GraphQL
    const response = await fetch("/graphql", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            query: `
                query {
                    daftarWisata {
                        id
                        nama
                        deskripsi
                        gambar
                    }
                }
            `
        })
    });

    const result = await response.json();
    const wisataList = result.data.daftarWisata;

    // Isi tabel dengan data yang diterima dari GraphQL
    const wisataDataContainer = document.getElementById("wisataData");
    wisataDataContainer.innerHTML = wisataList.map((wisata, index) => `
        <tr>
            <td>${index + 1}</td>
            <td><img src="${wisata.gambar}" alt="${wisata.nama}" width="100"></td>
            <td>${wisata.nama}</td>
            <td>${wisata.deskripsi}</td>
        </tr>
    `).join("");

    tabel.style.display = "table"; // Tampilkan tabel
});
