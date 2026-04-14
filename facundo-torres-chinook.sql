SELECT FirstName, LastName
FROM Employee
ORDER BY LastName, FirstName;

SELECT t.Name, t.Milliseconds
FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE a.Title = 'Big Ones'
ORDER BY t.Milliseconds DESC;

SELECT name,UnitPrice FROM tracks ORDER by 
UnitPrice  ASC LIMIT 10 

SELECT t.Name, g.Name, a.Title
FROM tracks t
JOIN genres g ON t.GenreId = g.GenreId
JOIN albums a ON t.AlbumId = a.AlbumId

SELECT t.Name, t.Milliseconds, a.Title, ar.Name
FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists ar ON a.ArtistId = ar.ArtistId
ORDER BY t.Milliseconds ASC
LIMIT 20;