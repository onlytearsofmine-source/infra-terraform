const fs = require('fs');
const path = require('path');

class TerraformParser {
  constructor(filePath) {
    this.filePath = path.resolve(filePath);
  }

  parse() {
    if (!fs.existsSync(this.filePath)) {
      throw new Error(`File not found: ${this.filePath}`);
    }

    const fileContent = fs.readFileSync(this.filePath, 'utf8');
    return this._parseContent(fileContent);
  }

  _parseContent(content) {
    try {
      return JSON.parse(content);
    } catch (error) {
      throw new Error(`Failed to parse JSON: ${error.message}`);
    }
  }

  static validateSchema(data, schema) {
    const Ajv = require('ajv');
    const ajv = new Ajv();
    const validate = ajv.compile(schema);

    if (!validate(data)) {
      throw new Error(`Schema validation failed: ${ajv.errorsText(validate.errors)}`);
    }

    return true;
  }
}

module.exports = TerraformParser;