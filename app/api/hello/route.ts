import { NextResponse } from "next/server";
// import { z } from "zod";

export async function GET(
  req: Request,
) {
  try {
    return NextResponse.json({data: "Hello Next.js TS API."}, { status: 200 });

  } catch (err) {
    return NextResponse.json(
      { error: "Internal Server Error" },
      { status: 500 },
    );
  }
}
