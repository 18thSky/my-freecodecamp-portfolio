--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: comet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.comet (
    comet_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text,
    is_visible boolean NOT NULL
);


ALTER TABLE public.comet OWNER TO freecodecamp;

--
-- Name: comet_comet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.comet_comet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comet_comet_id_seq OWNER TO freecodecamp;

--
-- Name: comet_comet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.comet_comet_id_seq OWNED BY public.comet.comet_id;


--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    name character varying(30),
    age_in_millions_of_years integer,
    distance_from_earth numeric,
    has_life boolean NOT NULL,
    is_spherical boolean NOT NULL,
    description text,
    galaxy_id integer NOT NULL
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    name character varying(30),
    age_in_millions_of_years integer,
    distance_from_earth numeric,
    has_life boolean NOT NULL,
    is_spherical boolean NOT NULL,
    description text,
    moon_id integer NOT NULL,
    planet_id integer
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    name character varying(30),
    age_in_millions_of_years integer,
    distance_from_earth numeric,
    has_life boolean NOT NULL,
    is_spherical boolean NOT NULL,
    description text,
    planet_id integer NOT NULL,
    star_id integer
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    name character varying(30),
    age_in_millions_of_years integer,
    distance_from_earth numeric,
    has_life boolean NOT NULL,
    is_spherical boolean NOT NULL,
    description text,
    star_id integer NOT NULL,
    galaxy_id integer
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: comet comet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.comet ALTER COLUMN comet_id SET DEFAULT nextval('public.comet_comet_id_seq'::regclass);


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: comet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.comet VALUES (1, 'Halley', 'Short-period comet visible every 75 years', true);
INSERT INTO public.comet VALUES (2, 'Hale-Bopp', 'One of the most widely observed comets', true);
INSERT INTO public.comet VALUES (3, 'Shoemaker-Levy 9', 'Broke apart and collided with Jupiter', false);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES ('Milky Way', 13600, 0, true, false, 'Our home galaxy', 1);
INSERT INTO public.galaxy VALUES ('Andromeda', 10000, 2500000, false, false, 'Nearest major galaxy', 2);
INSERT INTO public.galaxy VALUES ('Triangulum', 10000, 3000000, false, false, 'Small spiral galaxy', 3);
INSERT INTO public.galaxy VALUES ('Sombrero', 9000, 29000000, false, false, 'Looks like a hat', 4);
INSERT INTO public.galaxy VALUES ('Whirlpool', 10000, 23000000, false, false, 'Interacting grand design spiral', 5);
INSERT INTO public.galaxy VALUES ('Pinwheel', 11000, 21000000, false, false, 'Face-on spiral galaxy', 6);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES ('Moon', 4500, 0, false, true, 'Earths only moon', 1, 1);
INSERT INTO public.moon VALUES ('Phobos', 4500, 140, false, false, 'Fear', 2, 2);
INSERT INTO public.moon VALUES ('Deimos', 4500, 140, false, false, 'Dread', 3, 2);
INSERT INTO public.moon VALUES ('Io', 4500, 390, false, true, 'Volcanic moon', 4, 3);
INSERT INTO public.moon VALUES ('Europa', 4500, 390, false, true, 'Ice moon', 5, 3);
INSERT INTO public.moon VALUES ('Ganymede', 4500, 390, false, true, 'Largest moon', 6, 3);
INSERT INTO public.moon VALUES ('Callisto', 4500, 390, false, true, 'Cratered moon', 7, 3);
INSERT INTO public.moon VALUES ('Titan', 4500, 793, false, true, 'Has an atmosphere', 8, 4);
INSERT INTO public.moon VALUES ('Enceladus', 4500, 793, false, true, 'Ice geysers', 9, 4);
INSERT INTO public.moon VALUES ('Mimas', 4500, 793, false, true, 'Death star moon', 10, 4);
INSERT INTO public.moon VALUES ('Iapetus', 4500, 793, false, true, 'Two-toned moon', 11, 4);
INSERT INTO public.moon VALUES ('Dione', 4500, 793, false, true, 'Dense moon', 12, 4);
INSERT INTO public.moon VALUES ('Rhea', 4500, 793, false, true, 'Heavily cratered', 13, 4);
INSERT INTO public.moon VALUES ('Tethys', 4500, 793, false, true, 'Ice moon of Saturn', 14, 4);
INSERT INTO public.moon VALUES ('Titania', 4500, 1600, false, true, 'Largest of Uranus', 15, 7);
INSERT INTO public.moon VALUES ('Oberon', 4500, 1600, false, true, 'Outermost major moon', 16, 7);
INSERT INTO public.moon VALUES ('Umbriel', 4500, 1600, false, true, 'Dark moon', 17, 7);
INSERT INTO public.moon VALUES ('Ariel', 4500, 1600, false, true, 'Brightest moon', 18, 7);
INSERT INTO public.moon VALUES ('Miranda', 4500, 1600, false, true, 'Frankenstein moon', 19, 7);
INSERT INTO public.moon VALUES ('Triton', 4500, 2700, false, true, 'Retrograde orbit', 20, 8);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES ('Earth', 4500, 0, true, true, 'Our home', 1, 1);
INSERT INTO public.planet VALUES ('Mars', 4600, 140, false, true, 'The Red Planet', 2, 1);
INSERT INTO public.planet VALUES ('Jupiter', 4600, 390, false, true, 'Gas giant', 3, 1);
INSERT INTO public.planet VALUES ('Saturn', 4600, 793, false, true, 'Ringed planet', 4, 1);
INSERT INTO public.planet VALUES ('Venus', 4500, 25, false, true, 'Hottest planet', 5, 1);
INSERT INTO public.planet VALUES ('Mercury', 4500, 48, false, true, 'Smallest planet', 6, 1);
INSERT INTO public.planet VALUES ('Uranus', 4500, 1600, false, true, 'Ice giant', 7, 1);
INSERT INTO public.planet VALUES ('Neptune', 4500, 2700, false, true, 'Farthest planet', 8, 1);
INSERT INTO public.planet VALUES ('Proxima b', 4800, 4, false, true, 'Exoplanet', 9, 2);
INSERT INTO public.planet VALUES ('Kepler-22b', 4000, 600, false, true, 'Super Earth', 10, 2);
INSERT INTO public.planet VALUES ('Gliese 581g', 4300, 20, false, true, 'Unconfirmed planet', 11, 2);
INSERT INTO public.planet VALUES ('HD 209458 b', 4000, 150, false, true, 'Hot Jupiter', 12, 2);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES ('Sun', 4600, 0, false, true, 'Center of the solar system', 1, 1);
INSERT INTO public.star VALUES ('Sirius', 242, 8, false, true, 'Brightest star in the night sky', 2, 1);
INSERT INTO public.star VALUES ('Betelgeuse', 10, 642, false, true, 'Red supergiant', 3, 1);
INSERT INTO public.star VALUES ('Rigel', 8, 860, false, true, 'Blue supergiant', 4, 1);
INSERT INTO public.star VALUES ('Alpheratz', 60, 97, false, true, 'Brightest star in Andromeda', 5, 2);
INSERT INTO public.star VALUES ('Mirach', 10, 197, false, true, 'Red giant in Andromeda', 6, 2);


--
-- Name: comet_comet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.comet_comet_id_seq', 3, true);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 6, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 7, true);


--
-- Name: comet comet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.comet
    ADD CONSTRAINT comet_name_key UNIQUE (name);


--
-- Name: comet comet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.comet
    ADD CONSTRAINT comet_pkey PRIMARY KEY (comet_id);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_name_key UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

