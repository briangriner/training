-- Rutgers Oracle SQL/PLSQL, Java, Python Dev certification course

/* This is a multi line 
comment */

-- select * from Categories;
-- select * from Customers;
-- select * from Employees;
-- select * from Orders;
-- select * from Products;
-- select * from Shippers;
-- select * from Suppliers;

/* SELECT COLUMNS */
-- select CategoryName, Description from Categories;
-- select ContactName, CompanyName, ContactTitle, Phone from Customers;
-- select EmployeeID, Title, FirstName, LastName, Region from Employees;
-- select RegionID, RegionDescription from Region;
-- select CompanyName, Fax, Phone, HomePage from Suppliers;

/* order by queries */
-- select CategoryName, Description from Categories order by CategoryName;
-- select ContactName, CompanyName, ContactTitle, Phone from Customers order by Phone;
-- select FirstName, LastName, HireDate from Employees order by HireDate desc;
-- select OrderID, OrderDate, ShippedDate, CustomerID, Freight from Orders order by Freight desc;

/* where clause = */
-- select City from Customers;
-- select CompanyName, ContactName from Customers where City = 'Buenos Aires';
-- select ProductName, UnitPrice, QuantityPerUnit, UnitsInStock from Products where UnitsInStock = '0';
-- select OrderDate, ShippedDate, CustomerID, Freight from Orders where OrderDate = '1997-05-19';
-- select FirstName, LastName, Country from Employees where Country != 'USA'; 

/* where clause >, < */

/*
select EmployeeID, OrderID, CustomerID, RequiredDate, ShippedDate 
from Orders 
where ShippedDate > RequiredDate; 
*/
-- select City, CompanyName, ContactName from Customers where City < 'C';
-- select OrderID, Freight from Orders where Freight > '500.00';
-- select ProductName, UnitsInStock, UnitsOnOrder, ReorderLevel from Products where ReorderLevel > '0';

/* where clause NULL values */
-- select CompanyName, ContactName, Fax from Customers where Fax is not NULL; --!= '';
-- select FirstName, LastName, ReportsTo from Employees where ReportsTo is NULL;

/* where and order by clauses */
-- select CompanyName, ContactName, Fax from Customers where Fax is not null order by CompanyName;
-- select City, CompanyName, ContactName from Customers where City < 'C' order by ContactName desc;

/* more selects with where */
-- select FirstName, LastName, BirthDate from Employees where BirthDate like '195%';
/*
select SupplierID, CompanyName from Suppliers 
where CompanyName in ('Exotic Liquids', "Grandma Kelly's Homestead", 'Tokyo Traders');
*/
-- select ProductName, SupplierID from Products where SupplierID in (1, 3, 4);
-- select ShipPostalCode, OrderID, OrderDate from Orders where ShipPostalCode like '02389%';

-- not must come after where
-- select ContactName, ContactTitle, CompanyName from Customers where not ContactTitle like 'Sales%';

/* checking multiple conditions */
-- select * from Employees;
-- select FirstName, LastName, City, Region from Employees where City <> 'Seattle' and Region in ('WA');
/*
select CompanyName, ContactTitle, City, Country from Customers 
where Country = 'Mexico' or (Country = 'Spain' and City <> 'Madrid');
*/

/* calculated fields */
/*
select UnitPrice, Quantity, Discount, UnitPrice * Quantity * (1-Discount) as TotalPrice 
from `Order Details`;
*/
-- select concat(FirstName, ' ', LastName, 'can be reached at x', Extension) from Employees;

/* aggregate functions */
/*
select ProductID, sum(Quantity) as TotalUnits from `Order Details`
group by ProductID
having sum(Quantity) < 200;
*/

/*
select ProductID, avg(UnitPrice) as AveragePrice from Products
group by ProductID
having avg(UnitPrice) > 70
order by AveragePrice;
*/
/*
select CustomerID, count(OrderDate) as NumOrders
from Orders
group by CustomerID
having count(OrderDate) > 15
order by NumOrders desc;
*/

/* data manipulation functions */

/*
select UnitsInStock, UnitPrice, UnitsInStock * UnitPrice as TotalPrice, 
floor(UnitsInStock * UnitPrice) as TotalPriceDown, ceiling(UnitsInStock * UnitPrice) as TotalPriceUp
from Products
order by TotalPrice desc;	
*/
/*
select datediff(HireDate,BirthDate) / 365.25 as HireAgeAccurate1, 
(to_days(HireDate) - to_days(BirthDate))/ 365.25 as HireAgeAccurate2,
year(HireDate) - year(BirthDate) as HireAgeInaccurate
from Employees;
*/
/*
select FirstName, LastName, date_format(BirthDate, '%M') as BirthMonth
from Employees
where extract(month from BirthDate) = extract(month from now());
*/
-- select lower(ContactTitle) as Title from Customers;

/* subqueries */
/*
select ProductName, SupplierID from Northwind.Products
where SupplierID in (select SupplierID from Northwind.Suppliers 
where CompanyName in ( 'Exotic Liquids', 'Grandma Kelly''s Homestead', 'Tokyo Traders' ));
*/
/*
select ProductName from Northwind.Products
where CategoryID = (select CategoryID from Northwind.Categories where CategoryName = 'Seafood');
*/
/*
select CompanyName from Northwind.Suppliers
where SupplierID in (select SupplierID from Northwind.Products where CategoryID = '8');
*/
/* table alias can also reference DB name
select CompanyName from Northwind.Suppliers s 
where s.SupplierID in (select p.SupplierID from Northwind.Products p
where p.CategoryID in (select c.CategoryID from Northwind.Categories c where c.CategoryName = 'Seafood')); 
*/

/* joins */
/*
select o.OrderID, e.FirstName, e.LastName 
from Northwind.Orders o join Northwind.Employees e on (o.EmployeeID = e.EmployeeID)
where o.ShippedDate > o.RequiredDate;
*/
/*
select p.ProductName, sum(od.Quantity) as TotalUnits from Northwind.Order_Details od join Northwind.Products p 
on (od.ProductID = p.ProductID)
group by p.ProductName
having sum(od.Quantity) < '200';
*/
/*
select c.CompanyName, count(o.OrderID) as NumOrders from Northwind.Customers c join Northwind.Orders o
on (c.CustomerID = o.CustomerID) 
where o.OrderDate > '1996-12-31'
group by c.CompanyName
having count(o.OrderID) > '15'
order by NumOrders desc;
*/
/*
select c.CompanyName, od.OrderID, od.UnitPrice * od.Quantity * (1 - od.Discount) as TotalPrice from Northwind.Customers c 
join Northwind.Orders o on (c.CustomerID = o.CustomerID) join Northwind.Order_Details od
on (o.OrderID = od.OrderID)
where od.UnitPrice * od.Quantity * (1 - od.Discount) > '10000'
order by TotalPrice desc;
*/

/* outer joins & union */
/*
select concat(LastName, ' ', FirstName) as ContactName, HomePhone as Phone from Northwind.Employees
union
select ContactName, Phone from Northwind.Customers
union
select ContactName, Phone from Northwind.Suppliers
order by ContactName;
*/

/* case */
/*
select CompanyName, 
(case 
  when Fax is null 
  then 'No Fax'
  else Fax
end) as Fax
from Northwind.Customers
order by CompanyName;
*/




























