// ========================================
// BASE DE DATOS GEEK CLOTHING
// ========================================

// Crear y seleccionar la base de datos
use("GeekClothingDB");

// ========================================
// COLECCIÓN: USUARIOS
// ========================================

// Insertar un usuario
db.usuarios.insertOne({
    _id: 1,
    nombre: "David Quesada",
    correo: "david.quesada@geek-clothing.com",
    telefono: "88888888",
    fechaRegistro: new Date("2026-06-15")
});

// Insertar varios usuarios
db.usuarios.insertMany([
{
    _id: 2,
    nombre: "Ana Mora",
    correo: "ana.mora@geek-clothing.com",
    telefono: "87777777",
    fechaRegistro: new Date("2026-08-02")
},
{
    _id: 3,
    nombre: "Carlos López",
    correo: "carlos.lopez@geek-clothing.com",
    telefono: "86666666",
    fechaRegistro: new Date("2026-08-03")
},
{
    _id: 4,
    nombre: "María Rodríguez",
    correo: "maria.rodriguez@geek-clothing.com",
    telefono: "85555555",
    fechaRegistro: new Date("2026-08-04")
},
{
    _id: 5,
    nombre: "José Vargas",
    correo: "jose.vargas@geek-clothing.com",
    telefono: "84444444",
    fechaRegistro: new Date("2026-08-05")
},
{
    _id: 6,
    nombre: "Sofía Jiménez",
    correo: "sofia.jimenez@geek-clothing.com",
    telefono: "83333333",
    fechaRegistro: new Date("2026-08-06")
},
{
    _id: 7,
    nombre: "Luis Araya",
    correo: "luis.araya@geek-clothing.com",
    telefono: "82222222",
    fechaRegistro: new Date("2026-08-07")
},
{
    _id: 8,
    nombre: "Paula Chaves",
    correo: "paula.chaves@geek-clothing.com",
    telefono: "81111111",
    fechaRegistro: new Date("2026-08-08")
},
{
    _id: 9,
    nombre: "Daniel Solano",
    correo: "daniel.solano@geek-clothing.com",
    telefono: "80000000",
    fechaRegistro: new Date("2026-08-09")
},
{
    _id: 10,
    nombre: "Valeria Castro",
    correo: "valeria.castro@geek-clothing.com",
    telefono: "89999999",
    fechaRegistro: new Date("2026-08-10")
}
]);

// Registro de prueba para operaciones CRUD
db.usuarios.insertOne({
    _id: 99,
    nombre: "Usuario Temporal",
    correo: "temporal@geek-clothing.com",
    telefono: "70000000",
    fechaRegistro: new Date("2026-08-31")
});

// Actualizar usuario de prueba
db.usuarios.updateOne(
    { _id: 99 },
    {
        $set: {
            telefono: "79999999"
        }
    }
);

// Eliminar usuario de prueba
db.usuarios.deleteOne({
    _id: 99
});


// ========================================
// COLECCIÓN: MARCAS
// ========================================

// Insertar una marca
db.marcas.insertOne({
    _id: 1,
    nombre: "Kitsune Wear",
    pais: "Japón",
    colaboracion: "Ninja Legends"
});

// Insertar varias marcas
db.marcas.insertMany([
{
    _id: 2,
    nombre: "Titan Apparel",
    pais: "Japón",
    colaboracion: "Wall Guardians"
},
{
    _id: 3,
    nombre: "Saiyan Style",
    pais: "Japón",
    colaboracion: "Galactic Warriors"
},
{
    _id: 4,
    nombre: "Shadow Leaf Clothing",
    pais: "Japón",
    colaboracion: "Shinobi Chronicles"
},
{
    _id: 5,
    nombre: "Pirate King Outfitters",
    pais: "Japón",
    colaboracion: "Grand Voyage"
},
{
    _id: 6,
    nombre: "Soul Reaper Fashion",
    pais: "Japón",
    colaboracion: "Spirit Blades"
},
{
    _id: 7,
    nombre: "Alchemy Threads",
    pais: "Japón",
    colaboracion: "Steel Alchemists"
},
{
    _id: 8,
    nombre: "Hero Academy Wear",
    pais: "Japón",
    colaboracion: "Super Hero Generation"
},
{
    _id: 9,
    nombre: "Demon Hunter Gear",
    pais: "Japón",
    colaboracion: "Moon Breathing Saga"
},
{
    _id: 10,
    nombre: "Mecha Nexus",
    pais: "Japón",
    colaboracion: "Cyber Giant Project"
}
]);

// Marca de prueba CRUD
db.marcas.insertOne({
    _id: 99,
    nombre: "Otaku Wear Test",
    pais: "Japón",
    colaboracion: "Proyecto Temporal"
});

// Actualizar marca de prueba
db.marcas.updateOne(
    { _id: 99 },
    {
        $set: {
            colaboracion: "Proyecto CRUD Actualizado"
        }
    }
);

// Eliminar marca de prueba
db.marcas.deleteOne({
    _id: 99
});


// ========================================
// COLECCIÓN: PRENDAS
// ========================================

// Insertar una prenda
db.prendas.insertOne({
    _id: 1,
    nombre: "Camiseta Saiyan Evolution",
    marcaId: 3,
    categoria: "Camisetas",
    precio: 18000,
    stock: 50
});

// Insertar varias prendas
db.prendas.insertMany([
{
    _id: 2,
    nombre: "Sudadera Hoja Oculta",
    marcaId: 4,
    categoria: "Sudaderas",
    precio: 28000,
    stock: 35
},
{
    _id: 3,
    nombre: "Chaqueta Capitán Pirata",
    marcaId: 5,
    categoria: "Chaquetas",
    precio: 35000,
    stock: 20
},
{
    _id: 4,
    nombre: "Camiseta Academia Heroica",
    marcaId: 8,
    categoria: "Camisetas",
    precio: 17000,
    stock: 45
},
{
    _id: 5,
    nombre: "Hoodie Cazador de Demonios",
    marcaId: 9,
    categoria: "Sudaderas",
    precio: 30000,
    stock: 25
},
{
    _id: 6,
    nombre: "Camisa Alquimista Estatal",
    marcaId: 7,
    categoria: "Camisas",
    precio: 22000,
    stock: 30
},
{
    _id: 7,
    nombre: "Jacket Soul Reaper",
    marcaId: 6,
    categoria: "Chaquetas",
    precio: 38000,
    stock: 18
},
{
    _id: 8,
    nombre: "Playera Titan Defense",
    marcaId: 2,
    categoria: "Camisetas",
    precio: 19000,
    stock: 40
},
{
    _id: 9,
    nombre: "Camiseta Fox Spirit",
    marcaId: 1,
    categoria: "Camisetas",
    precio: 16000,
    stock: 55
},
{
    _id: 10,
    nombre: "Chaqueta Mecha Pilot",
    marcaId: 10,
    categoria: "Chaquetas",
    precio: 45000,
    stock: 15
}
]);

// Prenda de prueba CRUD
db.prendas.insertOne({
    _id: 99,
    nombre: "Camiseta Temporal",
    marcaId: 1,
    categoria: "Camisetas",
    precio: 10000,
    stock: 10
});

// Actualizar prenda de prueba
db.prendas.updateOne(
    { _id: 99 },
    {
        $set: {
            precio: 12000,
            stock: 15
        }
    }
);

// Eliminar prenda de prueba
db.prendas.deleteOne({
    _id: 99
});


// ========================================
// COLECCIÓN: VENTAS
// ========================================

// Insertar una venta
db.ventas.insertOne({
    _id: 1,
    usuarioId: 1,
    fecha: new Date("2026-08-20"),
    detalle: [
        {
            prendaId: 1,
            cantidad: 8
        }
    ],
    total: 144000
});

// Insertar varias ventas
db.ventas.insertMany([
{
    _id: 2,
    usuarioId: 2,
    fecha: new Date("2026-08-20"),
    detalle: [
        {
            prendaId: 4,
            cantidad: 5
        }
    ],
    total: 85000
},
{
    _id: 3,
    usuarioId: 3,
    fecha: new Date("2026-08-21"),
    detalle: [
        {
            prendaId: 5,
            cantidad: 4
        }
    ],
    total: 120000
},
{
    _id: 4,
    usuarioId: 4,
    fecha: new Date("2026-08-21"),
    detalle: [
        {
            prendaId: 1,
            cantidad: 6
        }
    ],
    total: 108000
},
{
    _id: 5,
    usuarioId: 5,
    fecha: new Date("2026-08-22"),
    detalle: [
        {
            prendaId: 8,
            cantidad: 7
        }
    ],
    total: 133000
},
{
    _id: 6,
    usuarioId: 6,
    fecha: new Date("2026-08-22"),
    detalle: [
        {
            prendaId: 7,
            cantidad: 3
        }
    ],
    total: 114000
},
{
    _id: 7,
    usuarioId: 7,
    fecha: new Date("2026-08-23"),
    detalle: [
        {
            prendaId: 3,
            cantidad: 5
        }
    ],
    total: 175000
},
{
    _id: 8,
    usuarioId: 8,
    fecha: new Date("2026-08-23"),
    detalle: [
        {
            prendaId: 9,
            cantidad: 6
        }
    ],
    total: 96000
},
{
    _id: 9,
    usuarioId: 9,
    fecha: new Date("2026-08-24"),
    detalle: [
        {
            prendaId: 10,
            cantidad: 2
        }
    ],
    total: 90000
},
{
    _id: 10,
    usuarioId: 10,
    fecha: new Date("2026-08-24"),
    detalle: [
        {
            prendaId: 2,
            cantidad: 9
        }
    ],
    total: 252000
}
]);

// Venta de prueba CRUD
db.ventas.insertOne({
    _id: 99,
    usuarioId: 1,
    fecha: new Date("2026-08-31"),
    detalle: [
        {
            prendaId: 1,
            cantidad: 1
        }
    ],
    total: 18000
});

// Actualizar venta de prueba
db.ventas.updateOne(
    { _id: 99 },
    {
        $set: {
            total: 20000
        }
    }
);

// Eliminar venta de prueba
db.ventas.deleteOne({
    _id: 99
});


// ========================================
// CONSULTAS
// ========================================

// ========================================
// CONSULTA 1
// ========================================

// Obtener la cantidad total de prendas vendidas en la fecha 2026-08-20

db.ventas.aggregate([
    {
        $match: {
            fecha: new Date("2026-08-20")
        }
    },
    {
        $unwind: "$detalle"
    },
    {
        $group: {
            _id: "$fecha",
            cantidadVendida: {
                $sum: "$detalle.cantidad"
            }
        }
    }
]);

// ========================================
// CONSULTA 2
// ========================================

// Obtener todas las marcas que poseen al menos una venta registrada

db.ventas.aggregate([
    {
        $unwind: "$detalle"
    },
    {
        $lookup: {
            from: "prendas",
            localField: "detalle.prendaId",
            foreignField: "_id",
            as: "prenda"
        }
    },
    {
        $unwind: "$prenda"
    },
    {
        $lookup: {
            from: "marcas",
            localField: "prenda.marcaId",
            foreignField: "_id",
            as: "marca"
        }
    },
    {
        $unwind: "$marca"
    },
    {
        $group: {
            _id: "$marca.nombre"
        }
    },
    {
        $project: {
            _id: 0,
            marca: "$_id"
        }
    }
]);

// ========================================
// CONSULTA 3
// ========================================

// Obtener cada prenda vendida junto con la cantidad restante disponible en inventario

db.ventas.aggregate([
    {
        $unwind: "$detalle"
    },
    {
        $group: {
            _id: "$detalle.prendaId",
            cantidadVendida: {
                $sum: "$detalle.cantidad"
            }
        }
    },
    {
        $lookup: {
            from: "prendas",
            localField: "_id",
            foreignField: "_id",
            as: "prenda"
        }
    },
    {
        $unwind: "$prenda"
    },
    {
        $project: {
            _id: 0,
            prenda: "$prenda.nombre",
            cantidadVendida: 1,
            stockInicial: "$prenda.stock",
            stockRestante: {
                $subtract: [
                    "$prenda.stock",
                    "$cantidadVendida"
                ]
            }
        }
    }
]);

// ========================================
// CONSULTA 4
// ========================================

// Obtener las 5 marcas más vendidas según la cantidad total de prendas comercializadas

db.ventas.aggregate([
    {
        $unwind: "$detalle"
    },
    {
        $lookup: {
            from: "prendas",
            localField: "detalle.prendaId",
            foreignField: "_id",
            as: "prenda"
        }
    },
    {
        $unwind: "$prenda"
    },
    {
        $lookup: {
            from: "marcas",
            localField: "prenda.marcaId",
            foreignField: "_id",
            as: "marca"
        }
    },
    {
        $unwind: "$marca"
    },
    {
        $group: {
            _id: "$marca.nombre",
            totalVentas: {
                $sum: "$detalle.cantidad"
            }
        }
    },
    {
        $sort: {
            totalVentas: -1
        }
    },
    {
        $limit: 5
    },
    {
        $project: {
            _id: 0,
            marca: "$_id",
            totalVentas: 1
        }
    }
]);

