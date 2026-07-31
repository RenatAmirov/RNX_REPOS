var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/hello", (string name = "ученик") => $"Привет, {name}!");

app.Run();