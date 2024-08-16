<script lang="ts">
    const tableArr = [
        {
            position: 1,
            name: "Bella",
            breed: "Siamese",
            adoptDate: new Date(2023, 3, 15)
        },
        {
            position: 2,
            name: "Luna",
            breed: "Maine Coon",
            adoptDate: new Date(2020, 7, 20)
        },
        {
            position: 3,
            name: "Oliver",
            breed: "Persian",
            adoptDate: new Date(2022, 1, 5)
        },
        {
            position: 4,
            name: "Simba",
            breed: "Ragdoll",
            adoptDate: new Date(2021, 10, 10)
        },
        {
            position: 5,
            name: "Chloe",
            breed: "British Shorthair",
            adoptDate: new Date(2021, 5, 25)
        },
        {
            position: 6,
            name: "Max",
            breed: "Sphynx",
            adoptDate: new Date(2024, 2, 12)
        },
        {
            position: 7,
            name: "Lucy",
            breed: "Bengal",
            adoptDate: new Date(2023, 11, 8)
        },
        {
            position: 8,
            name: "Charlie",
            breed: "Russian Blue",
            adoptDate: new Date(2021, 8, 30)
        },
        {
            position: 9,
            name: "Tiger",
            breed: "Scottish Fold",
            adoptDate: new Date(2022, 4, 18)
        },
        {
            position: 10,
            name: "Milo",
            breed: "Norwegian Forest Cat",
            adoptDate: new Date(2021, 6, 3)
        }
    ];
</script>

<div class="table-container">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Breed</th>
                <th>Adoption Date</th>
            </tr>
        </thead>
        <tbody>
            {#each tableArr as row, i}
                <tr>
                    <td>{row.position}</td>
                    <td>{row.name}</td>
                    <td>{row.breed}</td>
                    <td>{row.adoptDate.toLocaleDateString()}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>
