// Game Components
struct Commando {
    // Player stuff
	player_count: u8, // Could this be part of Commando?
	secret_code: u8,
	
	// Character stuff
    color: String, 
	probe: bool,
	red_card: bool,
	yellow_card bool,
	blue_card: bool,
	red_tool: bool,
	yellow_tool: bool,
	blue_tool: bool,
}

struct Probe {
    color: String, 
	probe: bool,
	red_card: bool,
	yellow_card bool,
	blue_card: bool,
}

// Map Stuff
struct Sector {
    color: String,
	is_open: bool,
	sector_rooms: Array,
}

struct Room {
    color: String,
	code: u8;
	sector; String,
	contents; tup, // Not sure if this is needed, or even appropriate >.>
	is_open; bool, // Just in case we need to close rooms as part of a sector shutdown.
}
