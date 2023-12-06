/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   header.cpp                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: del-yaag <del-yaag@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/04 20:24:27 by del-yaag          #+#    #+#             */
/*   Updated: 2023/12/06 18:52:46 by del-yaag         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <dirent.h>
#include <sys/types.h>

//colors
#define RESET   "\033[0m"
#define BLACK   "\033[30m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"

int main( void ) {

	DIR *dr;
	struct dirent *en;
	
	size_t findhpp;
	size_t findh;
	size_t findcpp;
	size_t findc;
	size_t findBy;
	size_t findCreated;
	size_t findUpdated;
	size_t findlogin;
	
	std::ifstream file;
	std::string login;

	std::cout << "enter login: ";
	getline( std::cin, login ).eof();
	if ( !login.length() )
		return 0;
		
	dr = opendir(".");
	if ( dr ) {

		while ( ( en = readdir( dr ) ) != NULL ) {

			std::string name = en->d_name;
			findcpp = name.find( ".cpp" );
			findc = name.find( ".c" );
			findhpp = name.find( ".hpp" );
			findh = name.find( ".h" );
			if ( findcpp != std::string::npos || findc != std::string::npos || findhpp != std::string::npos || findh != std::string::npos ) {
				
				bool cheat = 1;
				file.open( en->d_name );
				if ( !file ) {

					std::cout << "failed to open " << name << " file" << std::endl;
					return 1;
				}
				std::string buffer;
				while ( !getline( file, buffer ).eof() ) {
					
					findBy = buffer.find( "By: " );
					findCreated = buffer.find( "Created: " );
					findUpdated = buffer.find( "Updated: " );
					
					if ( findBy != std::string::npos ||
							findCreated != std::string::npos ||
							findUpdated != std::string::npos ) {

						findlogin = buffer.find( login );
						if ( findlogin == std::string::npos ) {

							cheat = 0;
							std::cout << RED << "cheater login in " << name << RESET << std::endl;
						} else {

							std::cout << GREEN << "ok " << name << RESET << std::endl;
						}
					}
				}
				if ( cheat ) std::cout << GREEN << name << " is OK!" << RESET << std::endl;
			}
			file.close();
		}
		closedir( dr );
	}
	return 0;
}