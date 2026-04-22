import type { Config } from "@jest/types";

const config: Config.InitialOptions = {
    preset: "ts-jest",
    testEnvironment: "node",
    testRegex: "integration-tests/.*\\.itest\\.ts$",
    transform: {
        "^.+\\.tsx?$": [
            "ts-jest",
            {
                tsconfig: "tsconfig.json",
            },
        ],
    },
    moduleFileExtensions: ["ts", "tsx", "js", "jsx", "json", "node"],
    moduleNameMapper: {
        "^(\\.\\.?\\/.*)\\.js$": "$1",
    },
};

export default config;
