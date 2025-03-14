USE [MLIAsolicitudes]
GO
/****** Object:  User [admin]    Script Date: 4/03/2025 4:53:43 p. m. ******/
CREATE USER [admin] FOR LOGIN [admin] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  Table [dbo].[Afiliado]    Script Date: 4/03/2025 4:53:43 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Afiliado](
	[ID_Prestamo] [int] IDENTITY(1000,1) NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
	[Edad] [tinyint] NOT NULL,
	[Ingresos_Anuales] [decimal](18, 2) NOT NULL,
	[Monto_Prestamo] [decimal](18, 2) NOT NULL,
	[Puntaje_Credito] [decimal](5, 2) NOT NULL,
	[Meses_Empleado] [smallint] NOT NULL,
	[Cantidad_Lineas_Credito] [tinyint] NOT NULL,
	[Tasa_Interes_Impuesto] [float] NOT NULL,
	[Duracion_Prestamo_Meses] [smallint] NOT NULL,
	[Relacion_Deuda_Ingresos] [float] NOT NULL,
	[Nivel_Educacion] [varchar](50) NOT NULL,
	[Estado_Laboral] [varchar](50) NOT NULL,
	[Estado_Civil] [varchar](50) NOT NULL,
	[Tiene_Hipoteca] [varchar](10) NOT NULL,
	[Tiene_Dependientes] [varchar](10) NOT NULL,
	[Proposito_Prestamo] [varchar](50) NOT NULL,
	[Tiene_CoFirmante] [varchar](10) NOT NULL,
	[Cumplimiento] [tinyint] NULL,
	[Estado_Solicitud] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_Prestamo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Licencias]    Script Date: 4/03/2025 4:53:43 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Licencias](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[clave] [nvarchar](100) NOT NULL,
	[fecha_creacion] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Usuarios]    Script Date: 4/03/2025 4:53:43 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Usuarios](
	[ID_Usuario] [int] IDENTITY(1,1) NOT NULL,
	[Nombre_Usuario] [varchar](50) NOT NULL,
	[Clave] [varchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_Usuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Licencias] ADD  DEFAULT (getdate()) FOR [fecha_creacion]
GO
