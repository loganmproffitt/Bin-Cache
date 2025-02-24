using Npgsql;
using System.IO;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Get the database connection string from appsettings.json
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

// Run SQL script at startup (only for dev/testing, not for production)
using (var connection = new NpgsqlConnection(connectionString))
{
    connection.Open();
    var script = File.ReadAllText("scripts/create_tables.sql");
    using (var command = new NpgsqlCommand(script, connection))
    {
        command.ExecuteNonQuery();
    }
}

app.Run();
