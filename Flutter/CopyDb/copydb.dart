// What This file Solves
// The file can be used to copy a existing database from assets folder of app  to internal folder of android where user cannot access it from file manager

// How to Integrate
// Add This file in your project

// Add The dependency to pubspec.yaml
// sqflite: ^2.2.4+1
// path_provider: ^2.0.12

// call the following method in init state where you would like to intilize and copy the database
// e.g DataBaseHelper.instance.initDb("test.db"); // here i am trying to copy test.db which is a sqlite3 database for my app

import 'dart:io';
import 'package:flutter/services.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart' as path;

class DataBaseHelper {
  static DataBaseHelper instance = DataBaseHelper();
  Database? database;

  Future initDb(String fileName) async {
    String baseDbPath = await getDatabasesPath();
    String dataBasePath = path.join(baseDbPath, fileName);
    bool isDatabasePresent = await databaseExists(dataBasePath);

    if (isDatabasePresent) {
      print("dataBase present already");
      database = await openDatabase(dataBasePath);
    } else {
      try {
        await Directory(path.dirname(dataBasePath)).create(recursive: true);
      } catch (e) {}
      ByteData data = await rootBundle.load(path.join("assets", fileName));
      List<int> bytes =
          data.buffer.asInt8List(data.offsetInBytes, data.lengthInBytes);
      await File(dataBasePath).writeAsBytes(bytes, flush: true);
      print("db copied at $dataBasePath");
    }
    database = await openDatabase(dataBasePath);
  }

  closeDataBase() async {
    await database?.close();
  }
}
